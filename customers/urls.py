from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers, name ="customers"),
    path('/update_customer/', views.upp_customer, name="update_customer")
]