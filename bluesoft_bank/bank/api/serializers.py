from rest_framework import serializers
from bank.models import Client, Account, Transaction
from typing import Any

class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Client model.
    """
    class Meta:
        model: Any = Client
        fields: Any = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for the Account model.
    """
    class Meta:
        model: Any = Account
        fields: Any = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transaction model.
    """
    class Meta:
        model: Any = Transaction
        fields: Any = '__all__'

