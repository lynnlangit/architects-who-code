# 1C / Data Security

WIP determining data security. Will use to figure out hardware/storage constraints/requirements

Current estimation: Apply encryption to all patient data at rest and in transit

## Status: 
WIP

## Context: 
In order to secure data both at at rest and in transit, we need a comprehensive approach to securing patient data end-to-end.

## Decision: 
- At rest - encrypt in all data storage location using internal KMS
- In transit - encrypt traffic on the wire using TLS 1.2+, HTTPS required for Dashboards
- Access control - each system (databases, services) to be configured to use strong authorization and authentication
- Network Boundaries - route via dedicated internal patient data network, physically separate from other networks, not connected to any external network, including public internet
- Auditing and logging - implement detailed logging of system access and alert on exception activities
- External Services - secure via VPN tunnel and network encryption, require service account authenticiation from hospital employee to perform PUSH
  
## Consequences: 
- Implementing extensive activity logging stresses the network and systems, requiring more performant databases and services, increasing cost to design, test, deploy and maintain while still meeting application latency requirements.
- The cost of setting up and maintaining a dedicated patient information network (in addition to the regular hosptial network for non-patient information) must be included in the budget.
- The cost of setting up an internal cerificate authority service to issue keys (KMS) must be included in the budget.  Encryption key rotation policies must be designed, performed and enforced via Organizational policy.
- We may chose to pay for a commercial event database (Aerospike) vs open source (Redis) as the former includes encryption at rest by default.  For the latter there is significant technical work needed to set up and maintain this capability.

## Considerations:
- Most hospitals do have internal user/service directory systems (i.e. Active Directory, ...)
- Most hospitals do NOT have KMS infrastructure/servers.
