from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,MaxLengthValidator,MinLengthValidator

# Create your models here.
class PizzaMenu(models.Model):
    name=models.CharField(max_length=50)
    ingredients=models.CharField(max_length=200)
    priceSmall=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(80)])
    priceBig=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(80)])

    def __str__(self):

        return self.name
    
class OrderModel(models.Model):
    pizzaName=models.CharField(choices=[(pizza.name, pizza.name) for pizza in PizzaMenu.objects.all()], max_length=100, blank=True, null=True)
    size=models.IntegerField(choices=[(32, '32'), (40, '40')])
    city=models.CharField(max_length=60)
    houseNumber=models.IntegerField()
    email=models.EmailField('email-field')
    phoneNumber=models.IntegerField()