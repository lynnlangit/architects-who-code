# 2A / Service Design

WIP determining service design. Will use to figure out service requirements from components

Current estimation: a cluster of service workers each run asynchronous stream readers. Broker takes care of (re)distributing messages across active clients.

![service layout](../images/services-layout.png)

## Status: 
WIP

## Context: 
In order to make services flexibile, we need to use microservices which are configured as small units of work for our application.

## Decision: 

The dev team has successfully designed multiple previous applications using microservices approaches.   
- Queues - throttle 
- Fetch - get data
- Disply - create viz
- Transform data - multiple scenarios - deidentify, xform for FIHR/HL7
- Push to external - push to two external services
  
## Consequences: 
- The cost of designing, coding, testing, deploying and maintaining multiple services must be included in the budget.
- The cost of supporting servers (hardware and storage) and load balancer servers (for high availabilty) must be included in the budget
- The cost of performing regular disaster recovery drills to verify that the failover solution works as expected must be included in the budget.
