# EcoTaxi Backend - Payment Service

EcoTaxi Backend - Payment Service is responsible for handling payment-related requests received from the API Gateway. Using [Django ORM](https://docs.djangoproject.com/en/5.1/), it interacts with a [MySQL](https://dev.mysql.com/doc/) database to securely store and retrieve payment information without requiring raw SQL queries.

## Git Repositories

This project is part of the EcoTaxi ecosystem, which includes multiple repositories for the frontend, backend services, and API gateway:v

- **Frontend**: [EcoTaxi Frontend](https://github.com/haiyen11231/eco-taxi-frontend.git)
- **API Gateway**: [EcoTaxi API Gateway](https://github.com/haiyen11231/eco-taxi-api-gateway.git)
- **User Service**: [EcoTaxi User Service](https://github.com/haiyen11231/eco-taxi-backend-user-service.git)
- **Payment Service**: [EcoTaxi Payment Service](https://github.com/AWYS7/eco-taxi-payment-service.git)
- **Trip Service**: [EcoTaxi Trip Service](https://github.com/lukea11/eco-taxi-backend-trip-service.git)

## Project Structure

```bash
eco-taxi-payment-service/
│
├── eco_taxi_backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── payment_service/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── grpc_server.py
│   ├── models.py
│   ├── repositories.py
│   └── serializers.py
│
├── proto/
│   ├── payment_service_pb2_grpc.py
│   ├── payment_service_pb2.py
│   └── payment_service.proto
│
├── .gitignore
├── app.env
├── Dockerfile
├── manage.py
├── requirements.txt
├── Makefile
└── README.md
```

## Prerequisites

Before you begin, ensure that you have the following installed:

- **Python**
- **gRPC Tools** (Protocol Buffers and gRPC Go)
- **MySQL**
- **Make**
- **Docker** (optional, for containerization)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AWYS7/eco-taxi-payment-service.git
   cd eco-taxi-payment-service
   ```

2. Create the app.env file:

Create a `app.env` file in the root directory of the project. This file should contain the environment variables required for the application to run. Here's a sample `app.env` file:

```env
# Database configuration
MYSQL_HOST=mysql_host
MYSQL_PORT=mysql_port
MYSQL_USER=mysql_user
MYSQL_PASSWORD=mysql_password
MYSQL_DATABASE=mysql_db

# gRPC configuration
GRPC_PORT=grpc_port

PORT=port
```

Update the values with your own configuration:

- **`MYSQL_*`**: MySQL configuration (host, port, user, password, and database).
- **`GRPC_PORT`**: Port on which the gRPC server for User Service will run (e.g., localhost:5004).
- **`PORT`**: Define the port number on which the User Service API will listen (e.g., 8083).

3. Install dependencies:

   ```bash
   make install
   ```

4. Start the development server:

   ```bash
   make run
   ```
