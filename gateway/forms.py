from django.core.exceptions import ValidationError
from django import forms
from django.forms import Textarea
from .models import Transaction

# for creating a transaction

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('order_id', 'cardnumber', 'customer_name', 'billing_postal', 'amount', 'merchant', 'transaction_type',)
