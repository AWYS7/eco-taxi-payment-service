import grpc
from concurrent import futures
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime
import os
import sys


# Add the project root and proto directory to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
sys.path.append(os.path.join(project_root, 'proto'))

# import AFTER proto directory
from proto import payment_pb2_grpc, payment_pb2

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxiweb_app.settings')
import django
django.setup()

from api.repositories import CardRepository


class PaymentService(payment_pb2_grpc.PaymentServiceServicer):

    def CreateCard(self, request, context):
        card_details = {
            'user_id': request.user_id,
            'card_number': request.card_number,
            'card_holder_name': request.card_holder,
            'expiry_date': datetime.fromtimestamp(request.expiry_date.seconds),
            'cvv': request.cvv,
            'is_default': request.is_default
        }
        CardRepository.create_card(card_details)
        return payment_pb2.CreateCardResponse(result="Card created successfully!")

    def GetCards(self, request, context):
        cards = CardRepository.get_cards(request.user_id)
        card_list = []
        for card in cards:
            expiry_date_proto = Timestamp()
            expiry_date_proto.FromDatetime(datetime.combine(card.expiry_date, datetime.min.time()))
            card_message = payment_pb2.Card(
                id=card.id,
                card_number=card.card_number,
                card_holder=card.card_holder_name,
                expiry_date=expiry_date_proto,
                cvv=card.cvv,
                is_default=card.is_default,
                user_id=int(card.user_id)
            )
            card_list.append(card_message)
        return payment_pb2.GetCardsResponse(result=card_list)

    def UpdateCard(self, request, context):
        card_details = {
            'card_number': request.card_number,
            'card_holder_name': request.card_holder,
            'expiry_date': datetime.fromtimestamp(request.expiry_date.seconds),
            'cvv': request.cvv,
            'is_default': request.is_default
        }
        updated_card = CardRepository.update_card(request.id, card_details)
        if updated_card:
            return payment_pb2.UpdateCardResponse(result="Card updated successfully!")
        else:
            return payment_pb2.UpdateCardResponse(result="Card not found!")

    def DeleteCard(self, request, context):
        deleted = CardRepository.delete_card(request.id)
        if deleted:
            return payment_pb2.DeleteCardResponse(result="Card deleted successfully!")
        else:
            return payment_pb2.DeleteCardResponse(result="Card not found!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Starting server...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
