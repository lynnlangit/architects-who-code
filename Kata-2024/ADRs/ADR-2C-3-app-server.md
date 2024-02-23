# 2C-3 / Service: application server

🚧 Error: time ran short for detailed diagram.

The application server exists to bridge the client and the data sources, as for multiple reasons we don't want (or simply can't) connect clients to data directly.

Other than supporting persistent connections to clients for real-time updates, the app server is a standard CRUD/REST server. See [ADR-2C-4 Clients](ADR-2C-4-app-clients.md) for more detail on persistent connections.

App traffic will be much lower than vitals traffic, and is relatively low-priority. A small number of cores running on all 3 service worker nodes should suffice. Need to benchmark.