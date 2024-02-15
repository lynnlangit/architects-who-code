# XYZ / Data Security

WIP determining data security. Will use to figure out hardware/storage constraints/requirements

Current estimation: Apply encryption to all patient data at rest and in transit

## Status: 
WIP

## Context: 
In order to secure data both at at rest and in transit, we need an approach to securing patient data end-to-end.

## Decision: 
- At rest - encrypt in all data storage location
- In transit - encrypt traffic on the wire
- Network Boundaries - Route via dedicated internal patient data network
- External Services - Secure via VPN tunnel and network encryption, require service account authenticiation from hospital employee to perform PUSH
  
## Consequences: 
- The cost of setting up and maintaining a dedicated patient information network (in addition to the regular hosptial network for non-patient information) must be included in the budget.
- Encryption key rotation policies must be designed, performed and enforced via Organizational policy.
