# Info about Devices

<img src="https://github.com/lynnlangit/architects-who-code/blob/main/Kata-2024/images/patient-devices.png" width=800>

## List of Medical-Grade Devices

1. Heart Rate Monitor
Device: Clinical-grade ECG machines, Telemetry monitors.
Data Format: ECG waveforms, numerical BPM; formats like HL7, DICOM, or proprietary hospital system formats.
Alert: Detect arrhythmias and cardiac abnormalities

2. Blood Pressure Monitor
Device: Automated sphygmomanometers used in hospitals.
Data Format: Numerical (mmHg) for systolic and diastolic readings; common formats include HL7 for integration with Electronic Health Records (EHRs).
Alert: hypertension

3. Oxygen Level Sensor (Pulse Oximeter)
Device: Hospital-grade pulse oximeters.
Data Format: Numerical SpO2 percentage; typically integrated into patient monitoring systems with HL7 or similar medical data formats.
Alert: Low O2

4. Blood Sugar Monitor
Device: Hospital-grade continuous glucose monitoring systems (CGMs).
Data Format: Numerical glucose readings; often integrated into EHRs with formats compatible with HL7.
Alert: Hypo/Hyperglycemia

5. Respiration Rate Sensor
Device: Capnography equipment or advanced patient monitoring systems.
Data Format: Numerical BPM; data often integrated into patient monitoring systems with formats like HL7.
Alert: Abnormal results

6. ECG Monitor
Device: Standard 12-lead ECG machines used in hospitals.
Data Format: ECG waveforms; typically stored and transmitted in DICOM (image) or HL7 formats.
Alert: Abnormal results

7. Body Temperature Sensor
Device: Electronic medical thermometers (oral, ear, rectal or temporary artery).
Data Format: Numerical (°C or °F); often integrated into patient monitoring systems, with HL7 being a common data format.
Alert: Abnormal body temperature

8. Sleep Status Monitor
Device: Polysomnography (PSG) equipment (used in sleep studies).
Data Format: Complex data including EEG(brain activity), ECG, EMG; typically in proprietary formats for sleep analysis, can be converted to HL7 for integration with other medical records - multi-channel waveform data.
Alert: Sleep Disorder

## Considerations for Device Data Integration:
- Data Integration: Most of these devices are designed to integrate with hospital information systems using standards like HL7, DICOM (images), or FHIR (patient data records).
- Interoperability: Ensure that the selected devices can communicate effectively with your cloud architectures and data pipelines.
- Data Security and Compliance: Adhere to relevant health data protection regulations (like HIPAA in the USA) and ensure secure data handling.
- Vendor Support: Choose devices from manufacturers that offer robust support and integration assistance.
