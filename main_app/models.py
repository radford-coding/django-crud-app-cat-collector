from django.db import models # type: ignore
from django.urls import reverse # type: ignore
# from django.db.models import Case, Value, When # type: ignore

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f'{self.name} ({self.id})' # id is given by Django as unique row in db

    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('cat-detail', kwargs={'cat_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
        # django provides the .get_ATTR_display() for CBV model ATTRibutes with predefined choices
    
    class Meta:
        ordering = ['-date'] # make newest feedings appear first
        # SQL: ... ORDER BY CASE 'B' THEN 1, CASE 'L' THEN 2, CASE 'D' THEN 3, ELSE 4


    