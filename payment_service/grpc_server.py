# Initialize Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eco_taxi_backend.settings')
import django
django.setup()
import grpc
from concurrent import futures
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime

import sys
from payment_service.repositories import CardRepository

# Add the project root and proto directory to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
sys.path.append(os.path.join(project_root, 'proto'))

# import AFTER proto directory
from proto import payment_service_pb2, payment_service_pb2_grpc

class PaymentService(payment_service_pb2_grpc.PaymentServiceServicer):
    def GetCards(self, request, context):
        try:
            print("Get Cards...")
            cards = CardRepository.get_cards(request.user_id)
            card_list = []
            for card in cards:
                expiry_date_proto = Timestamp()
                expiry_date_proto.FromDatetime(datetime.combine(card.expiry_date, datetime.min.time()))
                card_message = payment_service_pb2.Card(
                    id=card.id,
                    card_number=card.card_number,
                    card_holder=card.card_holder,
                    expiry_date=expiry_date_proto,
                    cvv=card.cvv,
                    is_default=card.is_default,
                    user_id=int(card.user_id)
                )
                card_list.append(card_message)
            return payment_service_pb2.GetCardsResponse(result=card_list)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            print(e)
            return payment_service_pb2.GetCardsResponse()  # return an empty response on error

    def CreateCard(self, request, context):
        try:
            print("Create Card...")
            print("request: ", request)
            card_details = {
                'user_id': request.user_id,
                'card_number': request.card_number,
                'card_holder': request.card_holder,
                'expiry_date': datetime.fromtimestamp(request.expiry_date.seconds),
                'cvv': request.cvv,
                'is_default': request.is_default
            }
            CardRepository.create_card(card_details)
            return payment_service_pb2.CreateCardResponse(result="Card created successfully!")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            print(e)
            return payment_service_pb2.CreateCardResponse()  # return an empty response on error

    def UpdateCard(self, request, context):
        try:
            print("Update Card...")
            card_details = {
                'card_number': request.card_number,
                'card_holder': request.card_holder,
                'expiry_date': datetime.fromtimestamp(request.expiry_date.seconds),
                'cvv': request.cvv,
                'is_default': request.is_default
            }
            updated_card = CardRepository.update_card(request.id, card_details)
            if updated_card:
                return payment_service_pb2.UpdateCardResponse(result="Card updated successfully!")
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Card not found!")
                return payment_service_pb2.UpdateCardResponse()  # return an empty response on error
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            print(e)
            return payment_service_pb2.UpdateCardResponse()  # return an empty response on error

    def DeleteCard(self, request, context):
        try:
            print("Delete Card...")
            deleted = CardRepository.delete_card(request.id)
            if deleted:
                return payment_service_pb2.DeleteCardResponse(result="Card deleted successfully!")
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Card not found!")
                return payment_service_pb2.DeleteCardResponse()  # return an empty response on error
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            print(e)
            return payment_service_pb2.DeleteCardResponse()  # return an empty response on error

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_service_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
    server.add_insecure_port('[::]:5004')
    server.start()
    print("Starting server...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()