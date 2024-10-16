import os
import sys
print("Starting server script...")  # Debugging message

# Ensure both project root and taxiweb folder are in the path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Initialize Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxiweb_app.settings')

import django
print("Setting up Django...")  # Debugging message

django.setup()

print("Django setup complete.")  # Debugging message


import grpc
from concurrent import futures
from proto import payment_pb2_grpc, payment_pb2
from api.repositories import CardRepository

class PaymentService(payment_pb2_grpc.PaymentServiceServicer):

    def ProcessPayment(self, request, context):
        user_id = request.user_id
        card_id = request.card_id
        amount = request.amount

        card = CardRepository.get_card_by_id(user_id, card_id)
        if not card:
            return payment_pb2.PaymentResponse(status="ERROR", message="Card not found!", amount=amount)

        if card.pay(amount):
            return payment_pb2.PaymentResponse(status="SUCCESS", message=f"Payment of {amount} processed successfully!", amount=amount)
        else:
            return payment_pb2.PaymentResponse(status="ERROR", message="Payment failed!", amount=amount)

    def AddCard(self, request, context):
        card_details = {
            'user_id': request.user_id,
            'card_id': request.card_id,
            'card_number': request.card_number,
            'card_holder_name': request.card_holder_name,
            'expiry_date': request.expiry_date,
            'cvv': request.cvv,
        }
        card = CardRepository.add_card(card_details)
        return payment_pb2.AddCardResponse(status="SUCCESS", message="Card added successfully!")

    def RemoveCard(self, request, context):
        user_id = request.user_id
        card_id = request.card_id

        result = CardRepository.remove_card(user_id, card_id)
        if result is None:
            return payment_pb2.RemoveCardResponse(status="ERROR", message="Card not found!")
        return payment_pb2.RemoveCardResponse(status="SUCCESS", message="Card removed successfully!")

    def UpdateCard(self, request, context):
        card_details = {
            'user_id': request.user_id,
            'card_id': request.card_id,
            'card_number': request.card_number,
            'card_holder_name': request.card_holder_name,
            'expiry_date': request.expiry_date,
            'cvv': request.cvv,
        }

        card = CardRepository.get_card_by_id(request.user_id, request.card_id)
        if card:
            # Update the card details and save
            card.card_number = request.card_number
            card.card_holder_name = request.card_holder_name
            card.expiry_date = request.expiry_date
            card.cvv = request.cvv
            card.save()
            return payment_pb2.UpdateCardResponse(status="SUCCESS", message="Card updated successfully!")
        else:
            return payment_pb2.UpdateCardResponse(status="ERROR", message="Card not found!")

    def GetCards(self, request, context):
        cards = CardRepository.get_cards(request.user_id)
        card_messages = [
            payment_pb2.Card(
                card_id=card.card_id,
                card_number=card.card_number,
                card_holder_name=card.card_holder_name,
                expiry_date=card.expiry_date
            ) for card in cards
        ]
        return payment_pb2.GetCardsResponse(cards=card_messages)

def serve():
    try:
        print("Starting the gRPC server...")  # Debugging message
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        payment_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
        print("Server configured, adding insecure port...")  # Debugging message
        server.add_insecure_port('[::]:5004')
        print("Port added, starting server...")  # Debugging message
        server.start()
        print("Server started successfully!")  # Debugging message
        server.wait_for_termination()
    except Exception as e:
        print(f"Exception occurred while starting the server: {e}")

if __name__ == "__main__":
    print("Running server...")  # Debugging message
    serve()
