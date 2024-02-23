# Information for O'Reilly Kata

Architectural Kata activity `MonitorMe` application challenge - Feb/Mar 2024. 

### CURRENT STATE / CHALLENGES: 
Hospital nurses and doctors need timely patient status in order to provide the highest quality patient care. Several **gaps exist** in the current US hospital market.  The first step in designing and building a new solution is to address these gaps by considering [current US hospital statistics](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/hospitals.md). Understanding challenges faced by medical professionals and those who support them in providing top quality hospital patient care the best starting point for this design process.
1. Nurses need to be immediately alerted to key pateient metrics from an aggregate patient monitoring system at the nurse's station **while they are working in any location in the hospital**.
   - Currently they must be 'in-room' to gather patient monitoring information from [individual patient dashboards](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/devices.md)
   - Aggregate patient dashboards at nurse's stations have latencies, inaccuracies or are non-existant
   - Wearable alert devices do not yet exist for nurses
   - 👨‍⚕️ [nurse user-story](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/user-stories.md#nurses) and [nurse-interview](https://www.youtube.com/watch?v=3mDUZpnXJJ4)
2. Doctors need to get **patient monitor status for abnormal states rapidly** via timely, relevant alerts.
   - Abnormal rating alerts, when available, have excess latency, downtime & aren't always focused on key patient metrics, resulting in alert fatigue.
   - 👩🏻‍⚕️ [doctor user-story](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/user-stories.md#doctors)
3. IT needs to get **monitor down status notifications rapidly** via timely, relevant alerts.
   - Downtime system alerts have excess latency, are unreliable & aren't always focused on key system metrics, resulting in alert fatigue.
   - 🧑‍💻 [IT user-story](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/domain-info/user-stories.md#it--system-maintainers)

----

### GOAL: 

<img src="https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/logo.png" width=200 align=left>

Design new `MonitorMe` applications to work with **existing in-room patient devices / individual patient monitors** deployed in US Hospitals.  Additional [Solution Requirements](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/ADRs/ADR-0-required-bilities.md#solution-requirements) and associated ranked solution capabilties.
1. Create ALERT app for nurses from patient information DASHBOARD application (per 20 patients max) per nurse with minimal latency which displays current hospital patient information input from 8 patients devices for max 500 patients per installation
2. Create ALERT app for doctors (abnormal patient device readings), create alerts for IT (dashboard down)
3. Create INTEGRATION app to prepare (transform)/push patient data to existing cloud-based SaaS Products (`MonitorThem` and `MyMedicalData`)

    
---

## Solution Concept 1a: Nurse's Alert Device

SOLUTION ONE-A: Alert device (concept shown below) for nurses 
- Shows info from key patient alerts on monitoring device for up to 5 patients  

<img src="images/nurse-alert.png" width=400>

## Solution Concept 1b: Central Patient Info Dashboard

SOLUTION ONE-B: Visual Dashboard (concept shown below) for monitoring personnel.  
**IMPORTANT: Monitoring team may or may not be nurses.** 
- Shows monitoring info per patient, info changes to next patient every 5 seconds
- Shows info from 8 patient monitoring devices for up to 20 patients per aggregate dashboard     

<img src="images/nurse-dashboard.png" width=500>

## Solution Concept 2a & b: Doctor's Patient Info Mobile Alerts

SOLUTION TWO: Alert Systems for Doctors and IT Professionals  
- Alerts on defined/customizable patient device thresholds to doctors mobile phone (concept shown below) as Alert Type A
- Alerts on dashboard application downtime to IT pro's mobile phone as Alert Type B

<img src="images/doctor-alert.png" width=400>

## Solution Concept 3: Integration with SaaS Applications
SOLUTION THREE: Integration Applications
- Integrator w/ individual Patient Record, then PUSH to external API 1 `MyMedicalData`
- Integrator w/Aggregate Patient Event Data, then PUSH to external API 2 `MonitorThem`

<img src="images/connected.png" width=400>

----

### Solution Components

Components shown in diagram below.  GREY are currently existing components, the SIX components shown inside the grey box will be built for the `MonitorMe` application.  
- Additional detailed solution diagrams for various pespectives are included in ADRs.
- List of ADRs is linked below and includes solution details.  

<img src="images/components.png">

### ADRs - List of related ADRs and links to documents
- [ADR-0:GENERAL - Restate Requirements and match Solutions characteristics (or `bilities)](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/ADRs/ADR-0-required-bilities.md)
- [ADR-1A:DATA - Forecast data volume and consider database types for data volume and types](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/ADRs/ADR-1A-data-volumes.md)
- [ADR-1B:DATA - Plan uptime SLO and consider database types and features for data availability](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/ADRs/ADR-1B-data-availability.md)
- [ADR-1C:DATA - Review security baseline and consider database types and features for data security](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/ADRs/ADR-1C-data-security.md)
- [ADR-2A:SERVICES - Review component baseline and consider service design pattern options](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/ADRs/ADR-2A-services-design.md)
- [ADR-2B:SERVICES - Review component availability and consider service design pattern options](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/ADRs/ADR-2B-services-availability.md)
- [ADR-3A:ENV - Review dev environment and team capabilties and consider language, tools and patterns](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/ADRs/ADR-3A-dev-env.md)
- [ADR-3B:ENV - Review physical environment and plan for required new hardware](https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/ADRs/ADR-3B-hardware.md)


----

### Team

- David Haley - https://www.linkedin.com/in/davidchaley/
- Lynn Langit - https://www.linkedin.com/in/lynnlangit/
- AI Partners - Gemini Pro Advanced + ChatGPT 4.0 + plugins (DALLE and others)



