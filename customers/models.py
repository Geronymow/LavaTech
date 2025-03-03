from django.db import models

class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.firstname
    
class Car(models.Model):
    car= models.CharField(max_length=50)
    plate = models.CharField(max_length=8)
    year = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    washing = models.IntegerField(default=0)
    repair = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.car