from django.shortcuts import render,redirect
from .models import Transaction
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'main/index.html')
@login_required(login_url='login')
def home(request):
    user=request.user
   
    contex={
        'user':user

    }
    return render(request,'main/home.html',contex)
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
def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('home')
        
   
    return render(request,'main/auth/login.html')
def sign_up(request):
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request,'main/auth/signup.html',{"form":form})
def log_out(request):
    logout(request)
    return redirect("index")
