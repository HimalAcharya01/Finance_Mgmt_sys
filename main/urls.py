from django.urls import path
from .views import index,profile,transaction_chart_data
urlpatterns = [
    path("",index),
    path("profile/",profile,name='profile'),
    path('api/transaction/',transaction_chart_data,name='transaction')
    
]


