# Rules for Device Data

- Collect device event data in device-native format
- Collect device event data at intervals per requirements per device
- Notify if device event data is NULL at requested interval
- Log if device event data is manually paused at requested interval
- Notify if device event data is outside of defined boundary at requested interval
- Generate and push alerts to nurses / dashboard and doctors / mobile when notifications fire

## Transformation for Device Data

- From HOT to WARM 
    - copy from HOT to WARM storage
    - remove from HOT storage AFTER successful copy
    - aggregate (tranform) by time interval
    - transform for FIHR/HL7 compatibility
- From WARM to COOL 
    - snapshot aggregate data
    - replicate from WARM to cool storage
- From COOL to COLD 
    - archive to cold storage
    - remove from WARM and COOL storage on successful archiving