# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Merchant, Transaction, User

from django.contrib import admin

class MerchantAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'merchant', 'transaction_type', 'amount', 'customer_name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'create_date', 'merchant')

# Register your models here.
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(User, UserAdmin)
