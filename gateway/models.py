# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Merchant(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Transaction(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=8)
    create_date = models.DateTimeField(auto_now=True)
    cardnumber = models.CharField(max_length=16)
    customer_name = models.CharField(max_length=100)
    billing_postal = models.CharField(max_length=5)
    amount = models.FloatField(default=0)

    # transaction types
    verification = 'v'
    sale = 's'
    credit = 'c'

    transaction_type_dict = (
        (verification, 'v'),
        (sale, 's'),
        (credit, 'c'),
    )

    transaction_type = models.CharField(
        max_length=1,
        choices=transaction_type_dict,
        default=sale,
    )

    # transaction statuses
    authorized = 'authorized'
    declined = 'declined'
    settled = 'settled'

    transaction_status_dict = (
        (authorized, 'authorized'),
        (declined, 'declined'),
        (settled, 'settled'),
    )

    transaction_status = models.CharField(
        max_length=10,
        choices=transaction_status_dict,
        default='settled'
    )

# did not do much with this

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
