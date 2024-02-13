# Information for O'Reilly Kata

Architectural Kata activity - Feb/Mar 2024.

## Team

- David Haley - https://www.linkedin.com/in/davidchaley/
- AI Parners - Gemini Advanced + ChatGPT

## Process Definition and Outputs
- Goal: Produce Architectural Design - not code - two processes are required. **DUE Feb 22.**
 
  - Part One: Produce **Architectural Characteristics List**, `bilities` - behavior of the system
    - **Operational/DevOps** - performance, reliability, security, scalability, elasticity, deployability - match `bilities to requirements
      - Key idea - 'just simple enough', i.e. are microservices needed?
      - Key idea - can we solve with 'design' OR 'architecture', i.e. security via encryption on a monolith, via other method for a microservice
   - Part Two: Produce a **Structural Design**, skaffolding which can be implemented - given the business/domain problem - Key Idea - 'create an architecture'
       - Part Two-a: `create a logical architecture` - create the initial core **components**. Tip: Use noun/verb names (use DDD)
         - Old way: Assign user stories, Anaylyze roles/responsibilities, Analyze characteristics (`bilities)
         - New way: **Workflow approach** --> create x, find y, sign z, watch aa, place bb, then `personify`, i.e. 'who should do each of these things?`
         - New way: **Event-Storming** --> actor/action approach, i.e. who: bidder, does what: views live video stream, views live bid stream; auctioneer, does what; system: does what?
         - Next: Careful choose names and determine object boundaries based on `bilities
       - Part Two-b: `create a physical architecture` - update architecture based on implementation design to design **services** from components
         - Example: Microservices / event-driven architecture
         
## Judges Criteria
Process: Pick top 10: semi-finals, then each team can update and create a 5 min video, then Pick top 3: winners  
  
 1. Clarity of narrative; tell a story, follow narrative arch, intro problem, share complication, peak/solution, resolution
     - prelude, vision, final video, biz require, strategy, arch, sequence diagrams, ADRs (architecture decision records)
     - requirements, architecture, ADRs
     - overview, vision, goals, use cases, arch char, design contraints, high/mid arch, milestones, ADRs
  2. Completeness of Solution
    - can a solution be built based on what is provided
   3. ID of Arch Characteristics
     - scope / justification (use Architecture Char & Styles Worksheets)
   4. **Diagrams** - use correctly! i.e. Sequence, etc... TIP: Use color as a dimension
     - several types of diagrams, name and scope
     - component, context, user journey, sequence, system, deployment, UI mockups 
   6. **ADRs** - from book `Fundamentals of Software Architecture` book
       - format - single page - one decion per file (title, status "accepted", context, decision, consequences)
       - scope - can be broad or narrow, details matter  
   7. Overall Solution - is the solution feasible, can we see the style in the solution
   8. 5-min Video (if in semifinals)

## Problem Statement
- preamble - `MonitorMe` w/two existing cloud SaaS products `MonitorThem` and `MyMedicalData` --> build new "MonitorMe" from 8 systems (monitor, record, analyze, alert)
- users
 - 500 patients max per instance
 - ??? doctors, nurses
 - any other users - auditors, non-medical
- requirements ACCURACY is extremely important, SECURE but not HIPPA / GDPR
  - Live (Devices) - 8 devices (devices from every 500ms to once per hour), av/response time 1 sec, dashboard, 20 patients per nurse station max, rotates between patients every 5 seconds. Device type and transmit rate shown below.
    - Heart Rate - 500 milliseconds
    - Blood Pressure - 1 hour
    - Oxygen Level - 5 seconds
    - Blood Sugar - 2 minutes
    - Respiration Rate - 1 second
    - Electrocariogram (ECG) - 1 second
    - Body Temperature - 5 minutes
    - Sleep Status (sleeping or awake) - 2 minutes
  - Store/Retrieve - 24 hours history, filter on time / vital sign
  - Alert/Notify - via issue, thresholds (including calculated for awake or asleeep), push to mobile & monitors (Doctors on phones, Nurses to dashboards)
  - Always on (HA if any of 8 devices fails, keep going with others)
  - Snapshots - gen on demand and upload to `MyMedicalData` (uses secure HTTP API call / secure cloud)
- additonal context
  - deploy on premise, must interact with SaaS cloud-based to send data (based in California) - will be installed in EACH hospital
  - platform, data stores and databases we will design SOFTWARE and HARDWARE complete system design
  - must be expandable for more devices in the future
  - data accuracy is vital - literally
  - new market - expect change
  - secure data - but not HIPPA or GDPR...


## Learning Resources
- Expert O'Reilly Playlist - `...book(s)` by Sam Newman
- `Learning Systems Thinking` by Diana Montalion
- `Communication Patterns` by Jacqui Read
- `....new course` by Jacqui Raed
- `....book(s)` by Neal Ford & Mark Richardson

### Previous Winners
- https://github.com/miyagis-forests/farmacy-food-kata
- https://github.com/ldynia/archcolider
- https://github.com/TheJedis2020/arch_katas_2020
- https://github.com/lookfwd/archkata
