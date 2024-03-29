# 1B / Data Availability

Determining data availability. Will use to figure out hardware/storage constraints/requirements

Current estimation: Physically cluster at least two servers for each data store for high availability.  

## Status: 
Reviewed, updated and continuing work given our decision to use RabbitMQ + MySQL.  Also see ADR for Hardware.

## Context: 
In order to make data highly available, we need to use data clusters which are configured for automatic failover in the event of unexpected downtime.

## Decision: 
- Event database as a Q - Use at least two physical services and associated storage.  Configure (and test) failover. Note time to recover.
- Working database use MySQL - Use at least two physical services and attached SAN.  Configure (and test) failover. Note time to recover.
- Archival storage use MySQL or file storage- Configure data lifecycle, offload 'old' data to archival storage to reduce failover time of hot / warm databases and to reduce cost.
  
## Consequences: 
- The cost of setting up and maintaining at least two new dedicated database clusters (hardware, storage and setup) must be included in the budget.
- The cost of performing regular disaster recovery drills to verify that the failover solution works as expected must be included in the budget.
