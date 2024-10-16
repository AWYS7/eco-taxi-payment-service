This project demonstrates the gRPC payment service using Django as the backend and a MySQL database for managing card payment methods. The project consists of a gRPC server that provides functionality for adding, updating, retrieving, and deleting card details. 

Project Structure
├── taxiweb
│   ├── api
│   │   ├── grpc_server.py         # gRPC server implementation
│   │   ├── grpc_client.py         # gRPC client for testing
│   │   ├── repositories.py        # Repository class for card operations
│   ├── proto
│   │   ├── payment.proto          # Proto definition for gRPC service
│   │   ├── payment_pb2.py         # Generated code from proto file
│   │   ├── payment_pb2_grpc.py    # Generated gRPC service code from proto file
│   ├── settings.py                # Django settings
└── README.md
