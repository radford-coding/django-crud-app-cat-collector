from django.db import models # type: ignore
from django.urls import reverse # type: ignore

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})' # id is given by Django as unique row in db

    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('cat-detail', kwargs={'cat_id': self.id})
    