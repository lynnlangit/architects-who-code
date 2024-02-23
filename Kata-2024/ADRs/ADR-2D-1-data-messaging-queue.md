# 2D-1 / Data: Messaging queues

MonitorMe is fundamentally asynchronous: to provide decoupling & performance. There are many ways to implement asynchronous systems. We landed on the RabbitMQ messaging system.

## Messages vs Events

Loosely speaking, the main difference between events & messages is that event systems are best-effort whereas message systems try to guarantee delivery.

Durability & accuracy are extremely important for us. It's not ok to lose messages, whether by skipping their delivery or evicting them from memory.

## RabbitMQ

RabbitMQ is a popular open-source broker, featuring very high throughput (10s of thousands of messages per second on a 3-node cluster). It provides traditional FIFO queues as well as replayable data streams.

### Queues

See also: [documentation](https://www.rabbitmq.com/docs/quorum-queues).

Queues remove messages once consumers acknowledge processing. This makes them suitable as a job queue.

Quorum queues provide strong [data safety properties](https://www.rabbitmq.com/docs/quorum-queues#data-safety). For example, the cluster does not acknowledge message publication until a quorum of clusters acknowledge it.

### Streams

See also: [documentation](https://www.rabbitmq.com/docs/streams).

Streams don't remove messages. Instead, they accumulate messages for multiple reads by multiple clients (which could even read the stream multiple times). Messages can be expired based on age. In our use case, since long-term data is available in SQL, we can likely expire the real-time queue after ~30min.

Streams enable an important feature: any number of clients can subscribe to the real-time feed. This includes the alerting system, but also services that persist to SQL, or the application backend to pass on to clients via WebSockets.

Streams have a specific failure mode, [documented by RabbitMQ here](https://www.rabbitmq.com/docs/streams#data-safety). TLDR, there's a very brief window of time when files are not flushed to disk, as controlled by the operating system. It is an extremely unlikely scenario. Nonetheless, we could mitigate further by aggressively reducing (or even zero'ing) the buffer size, to force more often or immediate flushes.

### Encryption

RabbitMQ does not natively encrypt at rest. We must rely on the operating system to encrypt the hard drive.

RabbitMQ does support SSL connections. We must always use SSL for data in transit.

## RabbitMQ Alternatives

RabbitMQ is specialized technology, requiring training for our dev teams, plus hospital IT teams to operate. (adding/removing cluster nodes, etc)

A simpler or more standard technology is preferable if possible. These authors are relatively less familiar with on-premise enterprise-grade message buses, and are not particularly attached to RabbitMQ in particular.

### NoSQL

Most NoSQL technologies either suffer from consistency/durability issues, or, require polling as they don't support notification. Redis for example is a tough choice because it's hard to make it durable.

### SQL

If we could get away with a SQL database polled by clients, we could have 1 cluster for the hot data and another for the full data. The issue we foresee is several clients hammering the DB with poll loops:

`select * from queue where time > my_last_read`. 

Still, SQL is very fast, and our data volume is relatively low.

This [2020 MySQL OLTP benchmarking on AWS](https://minervadb.com/wp-content/uploads/2020/10/MySQL-8-Performance-Benchmarking-on-Amazon-EC2.pdf) reports >7k reads/sec and >5k writes/sec. While OLTP is a pretty specific benchmark, these are well above our minimum requirements. The issue is, how does it perform when the DB enforces concurrency via table locking, etc. SQL is not designed to be a real-time event stream.
