# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Merchant, Transaction
from .forms import TransactionForm
from django.urls import reverse_lazy, reverse
from django.db.models import Count, Sum, Avg

# Create your views here.

# transaction form on main page

def transaction(request):

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            merchant_id = transaction.merchant_id
            transaction.save() # seems redundant?
            return HttpResponseRedirect(reverse('summary', kwargs={'merchant_id': merchant_id}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransactionForm()

    return render(request, 'index.html', {'form': form})

# summarizes transactions by merchant

def summary(request, merchant_id):

    total_sales = Transaction.objects.filter(merchant_id=merchant_id).filter(transaction_type='s').aggregate(Sum('amount')).get('amount__sum', 0.00)
#    total_credits = Transaction.objects.filter(merchant_id=merchant_id).filter(transaction_type='c').aggregate(Sum('amount')).get('amount__sum', 0.00)
    total_ct = Transaction.objects.filter(merchant_id=merchant_id).aggregate(Count('id')).get('id__count', 0.00)
    aov = Transaction.objects.filter(merchant_id=merchant_id).filter(transaction_type='s').aggregate(Avg('amount')).get('amount__avg', 0.00)

    merchant = Merchant.objects.get(pk=merchant_id)
    merchant_name = merchant.company_name

    context = {
            'total_sales': total_sales,
#            'total_credits': total_credits, not showing anything right now
            'total_ct': total_ct,
            'aov': aov,
            'merchant_name': merchant_name,
        }
    return render(request, 'success.html', context)
