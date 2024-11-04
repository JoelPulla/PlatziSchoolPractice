from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=10)
    model_car = models.CharField(max_length=15)
    year = models.DateField()
    
    def __str__(self) :
        return self.brand
    
class Dealrshep(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
