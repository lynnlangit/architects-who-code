# 0 Solution Requirements & Capabiilities

WIP capturing stated application requirements. Will use to select and map to application `bilities`

Current estimation: Translate and Assign to 3 parts of solution design.

## Status: 
WIP

## Context: 
Given solution requirements captured from the scenario provided, shown below.

### SOLUTION REQUIREMENTS:
  - ACCURATE data is extremely important, vital!
  - SECURE data but *NOT* HIPAA / GDPR
  - PERFORMANT near real-time, minimal latency
  - AVAILABLE always on (HA if any of 8 devices fails, keep going with others)
  - LOCAL install on premises, no cloud
  - ALERTS notify - at thresholds & conditionals, push to mobile & monitors (Doctors on phones, Nurses to dashboards)
  - QUERYABLE generate on-demand snapshots, filter on time/vital signs, keep 24 hr history
  - FLEXIBLE built for easy extensibility - change, growth, new devices...
  - COMPLETE serves and stores information, software and hardware solution
  - INTEROPERABLE with two SaaS data services - on Cloud in California region, via secure HTTP API calls

## Decision
`Bility prioritization based on stated requirements by application.    
There are 3 applications in this solution.  Building applications that can grow flexibly is also a requirement.  

### Applications 1 & 2. For Nurse's Dashboard / Alert System for Doctors & IT

#### A Priority
- Accuracy / Reliability - correctness and minimum latency (SLOs)
- Availability - redunandcy, system must failover and minimize downtown
- Performance - HOT data, extremely low latency
- Security - medical data requires end-to-end security
#### B Priority
- Scalability - Max 500 beds per installation, defined workload.  2% of US Hospitals w/ more than 500 beds will require multiple system installs.
- Elasticity - workload is relatively stable, not spikey.
- Deployability - deployment will be a one-time event, with some updates.

---

### Application 3.  Integration w/Saas & Snapshots

#### A Priority
- Accuracy / Reliability - correctness and minimum latency (SLOs)
- Security - to/from cloud - medical data to/from internet requires secure transfer patterns (VPN tunnel, authentication, data encryption...)
- Availability - redunandcy - needs redundancy to be highly available, with automatic failover

#### B Priority
- Performance - WARM data, 24 hour latency
- Scalability - predicatble workload
- Elasticity - predictable workload
- Deployability - components will be deployed as be a one-time event, with minimal updates.

----

### Other 4. Growth / Future Application Features

#### A Priority
- Accuracy / Reliability
- Security
- Deployability
- Elasticity / Flexibility - new devices

#### B Priority
- Availability
- Performance - COOL data, use de-identified / dummy patient data for dev / test
- Scalability

## Consequences
Must iterate and re-rank prioritization as more information is discovered during design phases of this project.

