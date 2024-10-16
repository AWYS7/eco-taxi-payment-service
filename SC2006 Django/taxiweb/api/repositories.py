from .models import CardPaymentMethod

class CardRepository:
    @staticmethod
    def add_card(card_details):
        card = CardPaymentMethod(**card_details)
        card.save()
        return card

    @staticmethod
    def remove_card(user_id, card_id):
        try:
            # Fetch the card by its card_id and delete it
            card = CardPaymentMethod.objects.get(user_id=user_id, card_id=card_id)
            card.delete()
        except CardPaymentMethod.DoesNotExist:
            return None  # If card is not found, return None or handle as needed

    @staticmethod
    def get_cards(user_id):
        return CardPaymentMethod.objects.filter(user_id=user_id)
    
    @staticmethod
    def get_card_by_id(user_id, card_id):
        try:
            return CardPaymentMethod.objects.get(user_id=user_id, card_id=card_id)
        except CardPaymentMethod.DoesNotExist:
            return None  # Handle card not found
