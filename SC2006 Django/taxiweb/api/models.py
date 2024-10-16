from django.db import models

class CardPaymentMethod(models.Model):
    # im assuming the user id will be coming from the user service
    # need to make sure the user id here matched user id in user service database
    # use foreign key?
    user_id = models.CharField(max_length=255,default='default_user') 
    card_id = models.CharField(max_length=255, unique=True)  
    card_number = models.CharField(max_length=16)  
    card_holder_name = models.CharField(max_length=255)
    expiry_date = models.CharField(max_length=5)  # format MM/YY 
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.card_holder_name} - {self.card_number[-4:]}'

    def pay(self, amount):
        """Simulate card payment processing. In real-world applications, integrate with a payment gateway."""
        print(f'Processing card payment of {amount} using card {self.card_number[-4:]}')
        return True  # Simulate success 
