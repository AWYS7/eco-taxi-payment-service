from rest_framework import serializers
from .models import CardPaymentMethod


class CardPaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardPaymentMethod
        fields= "__all__"