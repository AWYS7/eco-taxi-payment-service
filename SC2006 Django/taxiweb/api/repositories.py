from .models import CardPaymentMethod

class CardRepository:
    @staticmethod
    def create_card(card_details):
        card = CardPaymentMethod(**card_details)
        card.save()
        return card

    @staticmethod
    def get_cards(user_id):
        return CardPaymentMethod.objects.filter(user_id=user_id)

    @staticmethod
    def update_card(card_id, card_details):
        try:
            card = CardPaymentMethod.objects.get(id=card_id)
            for key, value in card_details.items():
                setattr(card, key, value)
            card.save()
            return card
        except CardPaymentMethod.DoesNotExist:
            return None

    @staticmethod
    def delete_card(card_id):
        try:
            card = CardPaymentMethod.objects.get(id=card_id)
            card.delete()
            return True
        except CardPaymentMethod.DoesNotExist:
            return False
