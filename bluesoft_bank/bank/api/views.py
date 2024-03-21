from rest_framework import generics
from bank.models import Client, Account, Transaction
from .serializers import ClientSerializer, AccountSerializer, TransactionSerializer
from typing import Any

class ClientList(generics.ListCreateAPIView):
    """
    View for listing and creating clients.
    """
    queryset: Any = Client.objects.all()
    serializer_class: Any = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a client.
    """
    queryset: Any = Client.objects.all()
    serializer_class: Any = ClientSerializer

class AccountList(generics.ListCreateAPIView):
    """
    View for listing and creating accounts.
    """
    queryset: Any = Account.objects.all()
    serializer_class: Any = AccountSerializer

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting an account.
    """
    queryset: Any = Account.objects.all()
    serializer_class: Any = AccountSerializer

class TransactionList(generics.ListCreateAPIView):
    """
    View for listing and creating transactions.
    """
    queryset: Any = Transaction.objects.all()
    serializer_class: Any = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting a transaction.
    """
    queryset: Any = Transaction.objects.all()
    serializer_class: Any = TransactionSerializer
