from django.contrib import admin # type: ignore
from .models import Cat, Feeding

# Register your models here.

admin.site.register(Cat)
admin.site.register(Feeding)