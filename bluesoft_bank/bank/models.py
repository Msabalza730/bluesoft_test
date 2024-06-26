from django.db import models


class Client(models.Model):
    """
    Model representing a client.
    """
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Account(models.Model):
    """
    Model representing a bank account.
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50) 
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    """
    Model representing a transaction.
    """
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50) 
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

