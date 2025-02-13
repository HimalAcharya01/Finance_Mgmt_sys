from django.shortcuts import render
from .models import Transaction
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'main/index.html')
def profile(request):
    return render(request,'main/profile.html')
def transaction_chart_data(request):
    transaction=Transaction.objects.all()
    category_type={}
    for transaction in transaction:
        category=transaction.category
        amount=float(transaction.transaction_amount)
        if category in category_type:
            category_type[category]+=amount
        else:
            category_type[category]=amount
    response_data={
        'labels':list(category_type.keys()),
        'data':list(category_type.values())
    }
    return JsonResponse(response_data)