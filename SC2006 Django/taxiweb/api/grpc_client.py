import grpc
import sys
import os

# Add the project root and proto directory to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
sys.path.append(os.path.join(project_root, 'proto'))

from proto import payment_pb2_grpc, payment_pb2
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = payment_pb2_grpc.PaymentServiceStub(channel)

        # Test CreateCard
        expiry_date = Timestamp()
        expiry_date.FromDatetime(datetime(2025, 12, 31))
        print("\nSending CreateCard request...")
        create_response = stub.CreateCard(payment_pb2.CreateCardRequest(
            user_id=1,
            card_number="4111111111111111",
            card_holder="James Doe",
            expiry_date=expiry_date,
            cvv=123,
            is_default=True
        ))
        print(f"CreateCard Response: {create_response.result}")

        # Test GetCards
        print("\nSending GetCards request...")
        get_cards_response = stub.GetCards(payment_pb2.GetCardsRequest(user_id=1))
        print("GetCards Response:")
        for card in get_cards_response.result:
            print(f"Card ID: {card.id}, Card Number: {card.card_number}, Holder: {card.card_holder}, Expiry: {card.expiry_date.seconds}, CVV: {card.cvv}")

        # Test UpdateCard
        expiry_date_update = Timestamp()
        expiry_date_update.FromDatetime(datetime(2026, 5, 15))
        print("\nSending UpdateCard request...")
        update_response = stub.UpdateCard(payment_pb2.UpdateCardRequest(
            id=get_cards_response.result[0].id,  # Using the ID from the first card returned in GetCards
            card_number="4222222222222222",  # New card number
            card_holder="Jane Doe",  # Updated card holder
            expiry_date=expiry_date_update,
            cvv=456,
            is_default=False
        ))
        print(f"UpdateCard Response: {update_response.result}")

        # Test GetCards 
        print("\nSending GetCards request after Update...")
        get_cards_response = stub.GetCards(payment_pb2.GetCardsRequest(user_id=1))
        print("GetCards Response after update:")
        for card in get_cards_response.result:
            print(f"Card ID: {card.id}, Card Number: {card.card_number}, Holder: {card.card_holder}, Expiry: {card.expiry_date.seconds}, CVV: {card.cvv}")

        # Test DeleteCard
        print("\nSending DeleteCard request...")
        delete_response = stub.DeleteCard(payment_pb2.DeleteCardRequest(
            id=get_cards_response.result[0].id  # Using the ID from the first card returned in GetCards
        ))
        print(f"DeleteCard Response: {delete_response.result}")

        # Test GetCards again after Delete
        print("\nSending GetCards request after Delete...")
        get_cards_response = stub.GetCards(payment_pb2.GetCardsRequest(user_id=1))
        if not get_cards_response.result:
            print("No cards found.")
        else:
            for card in get_cards_response.result:
                print(f"Card ID: {card.id}, Card Number: {card.card_number}, Holder: {card.card_holder}, Expiry: {card.expiry_date.seconds}, CVV: {card.cvv}")

if __name__ == "__main__":
    run()
