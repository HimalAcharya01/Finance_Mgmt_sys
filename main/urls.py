from django.urls import path
from .views import *
urlpatterns = [
    path("",index,name='index'),
    path("home/",home,name='home'),
    path("signup/",sign_up,name="signup"),
    path("login/",log_in,name="login"),
    path('api/transaction/',transaction_chart_data,name='transaction'),
    path("logout/",log_out,name='logout')
    
]


