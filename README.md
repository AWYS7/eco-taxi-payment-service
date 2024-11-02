This project demonstrates the gRPC payment service using Django as the backend and a MySQL database for managing card payment methods. The project consists of a gRPC server that provides functionality for adding, updating, retrieving, and deleting card details. 

## Project Structure
```bash
├── taxiweb
│   ├── api
│   │   ├── grpc_server.py         # gRPC server implementation
│   │   ├── grpc_client.py         # gRPC client for testing
│   │   ├── repositories.py        # Repository class for card operations
│   ├── proto
│   │   ├── payment.proto          # Proto definition for gRPC service
│   │   ├── payment_pb2.py         # Generated code from proto file
│   │   ├── payment_pb2_grpc.py    # Generated gRPC service code from proto file
│   ├──taxiweb_app
│       ├──settings.py        # Django settings
│
```
## Features
gRPC Server: Provides services to manage card payment methods and process payments.

Card Operations: Add, update, retrieve, and delete card details.

Payment Processing: Simulates processing a payment using stored card information.

MySQL Integration: Django ORM is used to interact with a MySQL database.

## Setting Up Environment
Set up your MySQL database and configure the settings.py under taxi_app

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'paymentdb',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

