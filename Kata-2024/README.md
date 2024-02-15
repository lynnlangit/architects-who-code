# Information for O'Reilly Kata

Architectural Kata activity `MonitorMe` application - Feb/Mar 2024. 

### CURRENT STATE/CHALLENGES: 
Timely patient status is vital to providing highest quality care, **gaps exist** in the [US hospital market](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/hospitals.md).  
1. Nurses need to **monitor up to 20 patients from their station**. Currently they must be 'in-room' to gather patient monitoring information from [individual patient dashboards](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/devices.md). Aggregate patient dashboards at nurse's stations have latencies, inaccuracies or are non-existant - [nurse user-story](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/user-stories.md#nurses)
2. Doctors need to get **patient monitor status for abnormal states rapidly**. Abnormal rating alerts, when available, have excess latency and downtime - [doctor user-story](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/user-stories.md#doctors)
3. IT needs to get **monitor down status notifications rapidly**. Downtime system alerts have excess latency and are unreliable - - [IT user-story](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/user-stories.md#it--system-maintainers)
    
### GOAL: 
Design new `MonitorMe` application to work with w/two existing cloud SaaS products `MonitorThem` and `MyMedicalData` and existing in-room patient devices / individual patient monitors.  
Additional [Solution Requirements](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/bilities.md#solution-requirements) and associated ranked solution capabilties.
1. Display current hospital patient information input from 8 patients devices for max 500 patients per installation 
2. Create patient information dashboards (per 20 patients max) per nurse with minimal latency
3. Create alerts for doctors (abnormal patient device readings), create alert for IT (dashboard down)
    
---
 
## Solution Concept: Nurse's Patient Info Dashboard

<img src="https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/nurse-dashboard.png" width=600>

- SOLUTION APPLICATIONS
  - PART ONE: Visual Dashboard (concept shown above) for nurses 
    - Shows monitoring info per patient, info changes to next patient every 5 seconds, shows info from 8 patient monitoring devices for up to 20 patients per nurse dashboard       
  - PART TWO: Alert Systems for Doctors and IT Professionals
    - Alerts on defined/customizable patient device thresholds to doctors mobile phone (concept shown below)
    - Alerts on dashboard application downtime to IT pro's mobile phone
  - PART THREE: Integration Applications
    - Integrator w/Patient Record, then PUSH to external API 1
    - Integrator w/Aggregate Event Data, then PUSH to external API 2

## Solution Concept: Doctor's Patient Info Mobile Alerts
   
<img src="https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/doctor-alert.png" width=600>

----
   
### Solution Components

Components shown in GREEN current exist, those shown in RED will be built for the `MonitorMe` application.
 - Process to capture patient device status event data --> (monitor, record, analyze, viz and/or alert)

<img src="https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/components.png" width=800>

----

### Team

- David Haley - https://www.linkedin.com/in/davidchaley/
- AI Parners - Gemini Advanced + ChatGPT



