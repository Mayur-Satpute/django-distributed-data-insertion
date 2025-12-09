from django.db import models

# Create your models here.

class User(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=80, null=True)
    email=models.EmailField()

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=80,null=True)
    price=models.FloatField(null=True)

class Order(models.Model):
    id=models.IntegerField(primary_key=True)
    user_id=models.IntegerField(null=True)
    product_id=models.IntegerField(null=True)
    quantity=models.IntegerField(null=True)