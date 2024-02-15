# XYZ / Data volumes

WIP determining data volume and storage. Will use to figure out hardware/storage constraints/requirements.

Current estimation: ![estimated data volumes](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/2024-Kata-data-volumes.png)

## Status: 
WIP

## Context: 
In order meet latency requirements, we need to use the fastest possible database as backing for our Dashboard application and associated Alert application.
Our dev team has previously succesfully built applications on MySQL.  They do not have experience with event-based databases.

## Decision: 
- Use event-based in-memory database for core applications to meet latency requirements
- Test open-source (Redis) and commercial (Aerospike) event databases
- Use relational database (MySQL) for intermediate storage and transformation before pushing to downstream databases (FIHR) and data services 

## Consequences: 
- Add training time for using event databases for dev team to budget.
- If open source events, we may spend excessive time setting up other required capabilities, i.e. failover clustering for high availability, snapshots, data encryption-at-rest, etc...
- If commercial events, we must consider licence cost as a tradeoff to be able to implement required features (listed above) more quickly, easily and reliably
