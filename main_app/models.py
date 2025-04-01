from django.db import models # type: ignore

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})' # id is given by Django as unique row in db

