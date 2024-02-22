# 2A / Service Design

WIP determining service design. Will use to figure out service requirements from components

The MonitorMe service design implements these components:

![components overview](../images/components.png)

This & related ADRs describe those components in more detail in order to design service implementation.

## Status: 
WIP

## Context: 
MonitorMe has 3 categories of components:

- patient data
- service workers & business logic
- application server & clients (nursing dashboard, mobile, etc.)

<insert diagram of 3 categories & relation>

Let's consider each.

### Patient data

The core patient data use cases can be grouped in two categories:

- real-time patient data collection, visualization, & alerting
- delay-tolerant patient data reporting, charting, & export

In both cases, security & privacy are key as this is sensitive personal health data. Note: we don't need to feed the **hipaa**potamus specifically for this kata.

### Service workers & business logic

MonitorMe is a distributed system, integrating with hundreds or even thousands of medical devices, not to mention a broader ecosytem of electronic health records both by StayHealthy Inc. and third-party vendors.

<img src="../images/in-room-monitor.png" width="300">

While some business logic is fairly static (example: the HL7 health data standard), other aspects of our solution are dynamic. Despite standardization, medical devices & monitoring stations all have their quirks. The sensor devices change as technology evolves. Our understanding of the customer will evolve. The customer's business processes will also evolve.

As such, it's important 

This ADR covers the services. (WIP high level overview)

![service layout](../images/services-layout.png)

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
