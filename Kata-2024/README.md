# Information for O'Reilly Kata

Architectural Kata activity - Feb/Mar 2024.

## Information about this Kata Challenge
- PROBLEM STATEMENTS: Timely patient status is vital to providing highest quality care, gaps exist in the market.
  - Nurses must be 'in-room' to gather patient monitoring information. Aggregate patient dashboards have latencies, inaccuracies or are non-existant.
  - Doctors need get patient monitor status for abnormal states rapidly. Abnormal Rating Alerts, when available, have excess latency and downtime.
  - IT needs to get monitor down status notifications rapidly. Downtime System Alerts have excess latency and are unreliable.
- GOAL: Design `MonitorMe` application to work with w/two existing cloud SaaS products `MonitorThem` and `MyMedicalData` 
  - display current hospital patient information input from 8 devices for max 500 patients per installation
  - create patient information dashboards (per 20 patients max) per nurse, create alerts for doctors, create alerts for IT
- REQUIREMENTS:
  - ACCURATE is extremely important, vital!
  - SECURE data, but *NOT* HIPPA / GDPR
  - PERFORMANT - near real-time
  - AVAILABLE - Always on (HA if any of 8 devices fails, keep going with others)
  - LOCAL install on premises
  - THRESHOLD-BASED ALERTING - Alert/Notify - via issue, thresholds (including calculated for awake or asleeep), push to mobile & monitors (Doctors on phones, Nurses to dashboards)
  - QUERYABLE - generate on-demand snapshots, filter on time/vital signs, keep 24 hr history
  - FLEXIBLE built for easy extensibility - change, growth, new devices...
  - COMPLETE serves and stores information, software and hardware solution
  - INTEROPERABLE with two SaaS data services - on Cloud in California region, via secure HTTP API calls
 
## Solution Design

<img src="https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/nurse-dashboard.png" width=600>

- SOLUTION: Visual Dashboard (concept shown above) for nurses and also alert system for doctors.
  - Shows monitoring info per patient, info changes to next patient every 5 seconds, shows info from 8 patient monitoring devices
  - Integrate with current existing systems
    - current in-room patient devices and individual patient monitor display
      - Live (Devices) - 8 devices (devices from every 500ms to once per hour), av/response time 1 sec, dashboard, 20 patients per nurse station max, rotates between patients every 5 seconds. Device type and transmit rate shown below.
        - Array of devices/montior rates to include: {Heart Rate - 500 milliseconds, BP - 1 hour, O2 - 5 seconds, Blood Sugar - 2 minutes, Respiration Rate - 1 second, ECG - 1 second, Temp - 5 minutes, Sleep Status (sleeping or awake) - 2 minutes}
        - Process to capture --> (monitor, record, analyze, alert)
   
### Solution Components

Components shown in GREEN current exist, those shown in RED will be built for the `MonitorMe` application.

<img src="https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/components.png" width=800>

### Team

- David Haley - https://www.linkedin.com/in/davidchaley/
- AI Parners - Gemini Advanced + ChatGPT



