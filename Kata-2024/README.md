# Information for O'Reilly Kata

Architectural Kata activity - Feb/Mar 2024.

## Problem Statement
- GOAL: Design `MonitorMe` application to work with w/two existing cloud SaaS products `MonitorThem` and `MyMedicalData` 
  - display current hospital patient information input from 8 devices (monitor, record, analyze, alert) for max 500 patients per installation
  - create dashboard for nurses, create alerts for doctors, create alerts for IT
- REQUIREMENTS:
  - ACCURACY is extremely important
  - SECURE but not HIPPA / GDPR
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
 
## Solution Design

<img src="https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/nurse-dashboard.png" width=800>

- SOLUTION: Visual Dashboard (concept shown above) for nurses and also alert system for doctors.
  - Integrate with current existing systems 

## Team

- David Haley - https://www.linkedin.com/in/davidchaley/
- AI Parners - Gemini Advanced + ChatGPT



