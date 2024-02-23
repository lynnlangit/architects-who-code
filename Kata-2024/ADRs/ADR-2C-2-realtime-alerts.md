# 2C-2 / Service: Real-time alerting

See also: [ADR-2A Service Design](ADR-2A-services-design.md)

The core task of the real-time alerts component is to read from the vitals stream, create alerts according to configuration, and deliver alerts to active or via push notifications to mobile devices. Staff interacts with the alert stream to acknowledge, close, escalate, & reroute alerts.

![Real-time alerts services](../images/component-2-realtime-alerts.png)

## Note on streams and queues

RabbitMQ [queues](https://www.rabbitmq.com/docs/quorum-queues) follow a normal produce-consume model: when a message is acknowleged as consumed, it goes away. This prevents multiple clients from receiving the same update.

In our case, many workers are interested in the vitals & alert data. Therefore we [Streams](https://www.rabbitmq.com/docs/streams) which may be read repeatedly by multiple clients. This makes them suitable to many clients subscribing to the feed.

## Vitals alerter

The vitals alerter is responsible for putting patients into alert states. Today, our requirements are simple: if a value is above or below a threshold, the patient is in alert state.

For some thresholds, the patient must be additionally awake (or asleep). To support this, the worker stores the most recent sleep status in memory. If it's not in memory (the worker booted after the last read was sent), the worker can fetch from earlier in the stream, or, from database. 

An alerter worker gets alert config (thresholds) from the database during initialization. To refresh threshold config, simply restart the worker.

Each service node runs an alerter worker. To simplify concurrency, we use the [single-active-consumer feature](https://www.rabbitmq.com/docs/streams#single-active-consumer). This means we always have one alerter running while the others are idle.

### Concerns

- **Throughput**. Single-active-consumer greatly simplifies concurrency. But it means we have 2 nodes of capacity sitting idle for HA purposes.
  - Checking a vital sign should be extremely fast, on the order of 10ms or less. It's simply receiving the message, checking against in-memory thresholds, and sending a message to the alert queue if necessary.
  - If 44 cores are dedicated to processing vitals for alerts, and it takes 10ms to process an alert, then we process 44 * (1000/10) = 4400 msg/s.
  - This is ~2x the average reads per second.
  - These assumptions need to be checked against a real environment.
- **Complexity**. Today's rules are simple. Tomorrow's, particularly AI trends analysis, will be more complex.
- **Trend alerts, not just instantaneous**. Threshold alerts are based on the instantaneous sensor value. In practice, better alerts likely need to account for the contextual trend.
- **More sublte alert state**. User research suggests we may want to distinguish between issues such as "no data present" vs "data present but bad". The former is likely a disconnected sensor and should be routed to a tech or medical assistant.

## Alert publisher

The alert publisher is responsible for interpreting the alert stream to send alerts.

While the client apps can read the alert stream directly to display alert status, the alert publisher ensures that proper notifications are routed & tracked. It tracks active alerts in the database to know whether or not to create a new push notification or resolve an existing one. It's also aware of who should receive which kind of alert via push notification.

As with the alerter, the publisher runs in single-active-consumer mode. Since alert traffic is small compared to vital signs, it should be sufficient to dedicate a single core.

### Concerns

- **Why a separate publisher?** The alerter could send push notifications itself. But its primary purpose is to evaluate alert status as fast as possible, which would be slowed by ACID/transactional handling of open alerts. An alternative could be pushing the alert in an async thread.
- **Build vs buy vs integrate**. Products like PagerDuty exist to manage alert routing, escalation policies, schedules, and so forth. Hospitals surely have tools to manage this based on active staff? We should consider integrating with an existing solution if possible.
