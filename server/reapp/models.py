from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255) # name varchar(255)
    price = models.IntegerField()
    description = models.TextField()
