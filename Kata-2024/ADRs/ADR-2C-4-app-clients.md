# 2C-4 / Service: application clients

🚧

Error: time ran short.

The client use cases:

- display patient data, alternating between patients if multiple are monitored
- receive patient data updates from the vitals stream (via the backend)
- alerts
  - display alert status based on alerts stream, as well as push notifications
  - allow staff to respond to alerts (acknowledge, close, redirect…)

The clients are straightforward in many respects. Here are the important parts:

- websocket / persistent connection to receive real-time updates from the server.
- regular CRUD/REST API for other operations.
- Ioniq, or similar, framework to target multiple devices.
- Might require specialized app for wearable device form factor; check with Design team.