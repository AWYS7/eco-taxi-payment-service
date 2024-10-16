import os
import sys
import grpc

# Add the root project directory to sys.path so that the proto module can be found
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from proto import payment_pb2_grpc, payment_pb2

def run():
    # Connect to the gRPC server
    print("Connecting to gRPC server...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = payment_pb2_grpc.PaymentServiceStub(channel)

        # Test RemoveCard request to remove the card before adding it again
        print("\nRemoving existing card before adding a new one...")
        remove_card_response = stub.RemoveCard(payment_pb2.RemoveCardRequest(
            user_id="1",
            card_id="1"
        ))
        print(f"RemoveCard Response: {remove_card_response.status} - {remove_card_response.message}")

        # Test AddCard request
        print("\nSending AddCard request...")
        add_card_response = stub.AddCard(payment_pb2.AddCardRequest(
            user_id="1",
            card_id="1",  # Card ID is reused after removal
            card_number="4111111111111111",
            card_holder_name="John Doe",
            expiry_date="12/25",  # Should match the proto field
            cvv="123"
        ))
        print(f"AddCard Response: {add_card_response.status} - {add_card_response.message}")

        # Test GetCards request
        print("\nSending GetCards request...")
        get_cards_response = stub.GetCards(payment_pb2.GetCardsRequest(user_id="1"))
        if get_cards_response.cards:
            print("GetCards Response: Found cards:")
            for card in get_cards_response.cards:
                print(f"  Card ID: {card.card_id}, Number: {card.card_number}, Holder: {card.card_holder_name}, Expiry: {card.expiry_date}")
        else:
            print("GetCards Response: No cards found.")

if __name__ == "__main__":
    run()
