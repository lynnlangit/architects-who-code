# 2B / Service Availability

WIP determining service availability. Will use to figure out hardware/storage constraints/requirements

Current estimation: Physically cluster at least two servers for each service for high availability.  Size servers appropriately to forecast workloads.  It may be possible to combine one or more services on a server cluster.

Most of this content is discussed through the other ADRs. This ADR should consolidate availability expectations & SLAs, etc.

## Status: 
WIP

## Context: 
In order to make services highly available, we need to use server clusters which are configured for automatic failover in the event of unexpected downtime. Front server clusters with network load balancers.

## Decision: 
- Server Clusters - Use at least three physical services with appropriately sized storage for one or more services.  Configure (and test) failover. Note time to recover.
  - Odd number of nodes provides resilience to network partitions.
- Network Load Balancers - Use an NLB for each server cluser.  Configure (and test) failover. Note time to recover.
- Reject k8s-style Container based clusters - adds complexity and is used for scenarios where rapid and extreme scale up/down is needed.  Our scenario workloads are more predictable. 
  Also current IT team is not familiar with container-based strategies - they currently use VM clusters.
- Use VM-style containers: basically http servers started & stopped by the OS like Apache. (Not pods like k8s)

## Consequences: 
- The cost of setting up and maintaining at least two new dedicated server clusters (hardware, storage and setup) must be included in the budget.
- The cost of performing regular disaster recovery drills to verify that the failover solution works as expected must be included in the budget.
