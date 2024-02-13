# Information for O'Reilly Kata

Architectural Kata activity - Feb/Mar 2024.

## Team

- David Haley - https://www.linkedin.com/in/davidchaley/
- AI Parners - Gemini Advanced + ChatGPT

## Process Definition and Outputs
- Goal: Produce Architectural Design - not code - two processes are required
 
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
   4. **Diagrams** - use correctly! i.e. Sequence, etc...
     - several types of diagrams, name and scope
   5. **ADRs** - from book `Fundamentals of Software Architecture` book
       - format - single page - one decion per file (title, status "accepted", context, decision, consequences)
       - scope - can be broad or narrow, details matter
## Problem Statement
- preamble
- users
- requirements
- additonal context


## Learning Resources
- Expert O'Reilly Playlist - `...book(s)` by Sam Newman
- `Learning Systems Thinking` by Diana Montalion
- `Communication Patterns` by Jacqui Read
- `....new course` by Jacqui Raed
- `....book(s)` by Neal Ford & Mark Richardson

- Previous Winners
- https://github.com/miyagis-forests/farmacy-food-kata
- https://github.com/ldynia/archcolider
- https://github.com/TheJedis2020/arch_katas_2020
- https://github.com/lookfwd/archkata
