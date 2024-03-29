# 2A / Service Design

WIP determining service design. Will use to figure out service requirements from components

The MonitorMe service design implements these components:

![components overview](../images/components.png)

This & related ADRs describe those components in more detail in order to design service implementation.

Here is the high-level service design, showing how the components interact via data or API.

![services, high level view](../images/services-highlevel.png)

## Status: 
WIP

## Context: 
MonitorMe has 3 categories of components:

- patient data
- service workers & business logic
- application server & clients (nursing dashboard, mobile, etc.)

Let's consider the service requirements for each.

### Patient data

The core patient data use cases can be grouped in two categories:

- real-time patient data collection, visualization, & alerting
- delay-tolerant patient data reporting, charting, & export

In both cases, security & privacy are key as this is sensitive personal health data. Note: we don't need to feed the **hipaa**potamus specifically for this kata.

The real-time data must be delivered & processed within a second, implying that the average delivery is well below 1s (or that response times are remarkably consistent). At maximum patient load with the current vitals configuration, MonitorMe produces 2.2K sensor readings per second on average. More precisely, it produces a lower but constant rate with occasional bursts. Here are the five minutes centered around the hour mark. The heart sensor is read the most often, once every 500ms for all 500 patients.

<img src="../images/data-points-500pts-zoomin.png" width=400>

See also [ADR-1A: data volumes](ADR-1A-data-volumes.md).

Whereas alerts presumably happen less frequently, they must also be identified, processed, & sent in real-time. Based on interviewing a nurse, a hospital could have hundreds of alerts a day, many of which are false positives such as accidentally disconnected sensors. See below for more on alerting business logic.

The delay-tolerant data usage is a fairly usual matter of fetching data for a certain time range, for a certain number of patients, displaying it in apps or the browser, and exporting it to external applications. While maximum patient load generates ~200M data points a day, it's only ~400k per patient. Assuming a 4-byte binary representation per point:

| Period | Total storage | Per-Patient |
| ---: | :--: | :--: |
| Per day | 800 MB | 1.6 MB |
| Per month | 24 GB | 48 MB |
| Per year | 292 GB | 584 MB |

While nothing to sneeze at, 300 GB fits 13 times into a commodity 4TB SSD. Well, fewer times, given DB indexes, overhead, etc. If we need to query more than 5 years into the past, we could provide a value-add data warehouse. It may also be acceptable to simply discard old data from MonitorMe if it's been integrated into the patient's electronic health record's database.

Beyond patient data, we also need to store application config & data, user data, and so forth.

### Service workers & business logic

MonitorMe is a distributed system, integrating with hundreds or even thousands of medical devices, not to mention a broader ecosytem of electronic health records both by StayHealthy Inc. and third-party vendors.

<img src="../images/in-room-monitor.png" width="300">

While some business logic is fairly static (example: the HL7 health data standard), other aspects of our solution are dynamic. Despite data standardization, medical devices & monitoring stations all have their quirks (example: different polling rates or APIs). We predict these areas to evolve:

- the sensors will change as technology evolves and new devices are deployed.
- we'll understand the customer better, for example we'll likely want to deliver smarter alerts using AI.
- the customer's business processes change with their IT needs, for example they may deploy a different electronic health records system.

To support this evolution we need modular software components and deployables. Updates must be easy for both MonitorMe developers & operators, requiring zero down-time.

Furthermore, the system is highly asynchronous. Patients come and go, vital sensors are put on and taken off. Connections are established and lost as patients are moved around the hospital. But these events have very small payloads (example: a heartbeat sensor update). The system should process available work as quickly as possible, without blocking on future work.

#### Alerting business logic

Alerting is so important to MonitorMe that it deserves its own section.

Alert logic varies by customer & over time. Hospitals may wish to customize alert thresholds based on clinical practices, or update following new medical recommendations.

Customer research (eg. nurse interview) tells us alert fatigue is a major problem. Systems alert too often, or incorrectly, or to the wrong person. Hospitals typically have sensor techs or medical assistants who handle the first alert triage, such as replacing a finger clip.

Alerts delivered in a vaccuum aren't helpful, for example "heart rate alert!" is less helpful than including the data trend or better yet an interpretation of that trend. Also, one patient's data going missing is likely an issue with the patient or the room, whereas a whole group of patients going offline might be a system issue requiring an IT alert.

While we want to roll out a basic version soon, we believe machine learning & AI will play a vital role in tuning alerting. Not only during detection (e.g. identifying abnormal trends) but also in the alerting (e.g. when to re-alert or escalate if no acknowledgment received). Our current alerting policies integrate sleep data with other vitals; we expect more vital signs to be integrated to provide even better alerts. We may also be able to leverage MonitorThem trends to suggest alerting policies.

### Application server & clients

Hospital staff interact with MonitorMe via mobile & smart watch applications, and a desktop interface deployed to nursing stations & other computers as necessary.

<img src="../images/doctor-alert.png" width=200> <img src="../images/nurse-dashboard.png" width=200><img src="../images/nurse-alert.png" width=200>

Hospitals have a variety of devices. Even if one hospital gives staff iPhones, another might provide Androids. We can probably assume the desktops are Windows machines, but might consider not depending on it.

Staff need access to alert status & notifications, as well as trend data from these applications. The larger-format devices would have sophisticated filtering on date or category, whereas the watch would likely display recent data.

The main complexity is receiving real-time updates. Otherwise, the apps & server are fairly standard. Server APIs should be mobile-friendly, for example supporting pagination, time range filters, and result size limits.

To avoid polling inefficiencies, real-time updates are communicated via persistent connections. This implies every device needs a persistent connection to a server. This can be accomplished with WebSockets or other technologies.

We should consider our client frameworks carefully. It would be costly to maintain several applications in several languages: Android in Kotlin, iOS in Swift, Windows in .NET… It may be worth up-skilling the development team to use a multi-platform framework such as Flutter, Ionic, or similar. Ionic for example supports both React & Angular frameworks, minimizing skills transfer required for the typical app developer.

## Decision: 

- Real-time data: RabbitMQ cluster with several queues (vitals, alerts, jobs, etc.)

  - [ADR-2D-1: Data: **Messaging queue**](ADR-2D-1-data-messaging.md)

- Long-term data: MySQL cluster

  - [ADR-2D-2: Data: **SQL database**](ADR-2D-2-data-sql.md)

- Service components:

  - **Backends**: Docker containers running as standard daemons
  - **Client apps**: Ionic w/ React

    - While Ionic can target Apple & Android wearables, we should consult our Design team whether we can use a single responsive app, or a dedicated watch app

  - [ADR-2C-1: Services: **Real-time vitals**](ADR-2C-1-realtime-vitals.md)

    [ADR-2C-2: Services: **Real-time alerts**](ADR-2C-2-realtime-alerts.md)

    [ADR-2C-3: Services: **App server**](ADR-2C-3-app-server.md)

    [ADR-2C-4: Services: **App clients**](ADR-2C-4-app-clients.md)

    [ADR-2C-5: Services: **Long-term data**](ADR-2C-5-longterm-data.md)

    [ADR-2C-6: Services: **Data export**](ADR-2C-6-data-export.md)


![service layout](../images/services-highlevel.png)

## Consequences: 
- The cost of designing, coding, testing, deploying and maintaining multiple services must be included in the budget.
- The cost of supporting servers (hardware and storage) and load balancer servers (for high availabilty) must be included in the budget
- The cost of performing regular disaster recovery drills to verify that the failover solution works as expected must be included in the budget.
