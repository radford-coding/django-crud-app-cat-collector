from django.contrib import admin # type: ignore
from .models import Cat

# Register your models here.

admin.site.register(Cat)