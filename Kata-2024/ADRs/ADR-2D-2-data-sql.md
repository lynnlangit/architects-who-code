# 2D-2 / Data: SQL Database

MonitorMe stores its data in a traditional SQL database. The SQL database contains application & user configuration as it would in any other app. It also contains a slightly-delayed record of the real-time stream as recorded in [ADR-2C-5 Long-term data](ADR-2C-5-longterm-data.md).

We chose MySQL because we believe it has better, native support for DB clustering.

This document is sparse, as we believe for now there is nothing particularly unusual about the SQL datastore:

- most developers have experience working with a SQL backend
- MySQL is a standard tech, well-understood by DBAs
- the data is straightforwardly indexed by patient ID, timestamp, and vital type
- the vast majority of SQL store calls are for delay-tolerant use cases such as loading reports, historical data, exporting to external services, etc.