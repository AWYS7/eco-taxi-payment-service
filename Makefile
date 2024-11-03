gen:
	python3 -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/payment_service.proto


clean:
	rm -f ./proto/*_pb2.py ./proto/*_pb2_grpc.py

migrate:
	python3 manage.py migrate

install:
	pip install -r requirements.txt

run:
	# python3 manage.py runserver  #by default 8000
	# python3 manage.py runserver 8083
	python -m payment_service.grpc_server


	# makemigrations 
