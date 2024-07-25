from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=50)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    published_at = models.DateTimeField(null=True)

# title , description , author, price , quantity, created_at
