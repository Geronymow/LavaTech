from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Customer,Car
from django.core import serializers
import json
import re

def customers(request):
    if request.method == "GET":
        customers_list = Customer.objects.all()
        return render(request, 'customers.html', {'customers': customers_list})
    elif request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        cars = request.POST.getlist('car')
        plates = request.POST.getlist('plate')
        years = request.POST.getlist('year')

        customer = Customer.objects.filter(cpf=cpf)

        if customer.exists():
            return render(request, 'customers.html', {'firstname': firstname, 'lastname': lastname, 'email': email, 'cars': zip(cars,plates,years)})

        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'customers.html', {'firstname': firstname, 'lastname': lastname, 'cpf': cpf, 'cars': zip(cars,plates,years)}) 
        
        customer = Customer(
            firstname = firstname,
            lastname = lastname,
            email = email,
            cpf = cpf
        )

        customer.save()

        for car, plate, year in zip(cars, plates, years):
            car = Car(car=car, plate=plate, year=year, customer=customer)
            car.save()

        return HttpResponse('test')
    


def upp_customer(request):
    id_customer = request.POST.get('id_customer')
    customer = Customer.objects.filter(id=id_customer)
    customer_json = json.loads(serializers.serialize('json',customer))[0]['fields']
    return JsonResponse(customer_json)