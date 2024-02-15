# 3B / Hardware

WIP determining production environment. Will use to figure out minimum new hardware constraints/requirements

Current estimation: Purchase new servers, appropriately sized, as shown in green areas on diagram below.

<img src="https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/hardware.png" width=800>

## Status: 
WIP

## Context: 
In order to deploy `MonitorMe` on premise meeting the performance, reliability and security requirements, we select, purchase and deploy a number of new servers to the production environment.

## Decision: 
- Database - deploy two, appropriately-sized servers to build a failover database cluster.  Depending on final selection of database, it maybe be neccesary to add to third server (if Redis) at minimum.  Load test and purchase appropirately sized fast disks to meet latency requirements.
- Services - deploy two, appropriately-sized compute clusters. Use load balancers for HA.
- Encryption - deploy lightweight KMS / CA solutions. Deploy root CA and issuing CA.  Consider adding redundancy for HA.
  
## Consequences: 
- Time to select, order, receive, setup and configure new hardware may impact project schedule.
- Adequate Load testing prior to selecting hardware is critical to selecting appropriately-sized hardware.

## Considerations / Questions:
- More new servers may be required to meet HA requirements.  For example, interal CA/KMS does not have redundancy at this time.
- Redundant power supplies will also need to be purchased to meet HA requirements.





