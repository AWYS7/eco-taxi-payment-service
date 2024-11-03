from django.db import models

class CardPaymentMethod(models.Model):
    user_id = models.BigIntegerField()
    card_number = models.CharField(max_length=16)
    card_holder = models.CharField(max_length=255)
    expiry_date = models.DateField()
    cvv = models.IntegerField()
    is_default = models.BooleanField()

    def __str__(self):
        return f'{self.card_holder_name} - {self.card_number[-4:]}'
