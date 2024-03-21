from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from models import *
from typing import Any, Dict

class ClientTests(TestCase):
    """
    Tests for Client model and API endpoints.
    """

    def setUp(self) -> None:
        """Set up initial data for tests."""
        self.cliente1: Client = Client.objects.create(name='Client 1', city='City1')
        self.cliente2: Client = Client.objects.create(name='Client 2', city='City2')

    def test_list_clients(self) -> None:
        """Test listing all clients."""
        response: Any = self.client.get(reverse('cliente-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_client(self) -> None:
        """Test retrieving a specific client."""
        response: Any = self.client.get(reverse('cliente-detail', kwargs={'pk': self.cliente1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Client 1')

class AccountTests(TestCase):
    """
    Tests for Account model and API endpoints.
    """

    def setUp(self) -> None:
        """Set up initial data for tests."""
        self.client1: Client = Client.objects.create(name='Client 1', city='City1')
        self.account1: Account = Account.objects.create(client=self.client1, account_type='Savings', balance=1000)

    def test_list_accounts(self) -> None:
        """Test listing all accounts."""
        response: Any = self.client.get(reverse('cuenta-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_account(self) -> None:
        """Test retrieving a specific account."""
        response: Any = self.client.get(reverse('cuenta-detail', kwargs={'pk': self.account1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tipo'], 'Savings')

class TransaccionTests(TestCase):
    """
    Tests for Transaccion model and API endpoints.
    """

    def setUp(self) -> None:
        """Set up initial data for tests."""
        self.client1: Client = Client.objects.create(name='Client 1', city='City1')
        self.account1: Account = Account.objects.create(client=self.account1, account_type='Savings', balance=1000)
        self.transaction1: Transaction = Transaction.objects.create(account=self.account1, transaction_type='Deposit', value=500)

    def test_list_transactions(self) -> None:
        """Test listing all transactions."""
        response: Any = self.client.get(reverse('transaccion-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_transaction(self) -> None:
        """Test retrieving a specific transaction."""
        response: Any = self.client.get(reverse('transaccion-detail', kwargs={'pk': self.transaction1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['valor'], '500.00')

