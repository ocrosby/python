# Location Microservice

## Overview

This service is responsible for storing and managing the location data of the users. 

It provides the following functionalities:

- Store the location data of the users
- Retrieve the location data of the users
- Update the location data of the users
- Delete the location data of the users

## API Endpoints

The service provides the following API endpoints:

- `POST /location` - Store the location data of the users
- `GET /location` - Retrieve the location data of the users
- `PUT /location` - Update the location data of the users
- `DELETE /location` - Delete the location data of the users
- `GET /health` - Check the health of the service
- `GET /info` - Get the information about the service
- `GET /metrics` - Get the metrics of the service
- `GET /ready` - Check if the service is ready to serve the requests
- `GET /live` - Check if the service is live
- `GET /version` - Get the version of the service
- `GET /config` - Get the configuration of the service
- `GET /env` - Get the environment variables of the service
- `GET /logs` - Get the logs of the service
- `GET /trace` - Get the traces of the service

## Database

The service uses a PostgreSQL database to store the location data of the users.

## Dependencies

The service depends on the following services:

- PostgreSQL - To store the location data of the users
- Kafka - To publish the events
- Redis - To cache the data
- Prometheus - To collect the metrics
- Grafana - To visualize the metrics
- Jaeger - To trace the requests
- Kiali - To monitor the service mesh


## Development

To run the microservice in development mode, execute the following command:

```bash
fastapi dev main.py
```

