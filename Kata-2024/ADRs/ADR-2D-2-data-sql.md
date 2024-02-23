# 2D-2 / Data: SQL Database

MonitorMe stores its data in a traditional SQL database. The SQL database contains application & user configuration as it would in any other app. It also contains a slightly-delayed record of the real-time stream as recorded in [ADR-2C-5 Long-term data](ADR-2C-5-longterm-data.md).

We chose MySQL because we believe it has better, native support for DB clustering.

This document is sparse, as we believe for now there is nothing particularly unusual about the SQL datastore:

- most developers have experience working with a SQL backend
- MySQL is a standard tech, well-understood by DBAs
- the data is straightforwardly indexed by patient ID, timestamp, and vital type
- the vast majority of SQL store calls are for delay-tolerant use cases such as loading reports, historical data, exporting to external services, etc.

## Retention

As per [ADR-2A: Services Design](ADR-2A-services-design.md), we can easily store several years of patient data on relatively small SSDs. Still, we must consider what happens as customers approach that limit after years of use.

We should provide a simple administrative tool that selects the oldest data from SQL, writes it to a log file (or better yet, data warehouse), then discards it from SQL.