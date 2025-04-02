from django.shortcuts import render # type: ignore
# from django.http import HttpResponse # type: ignore
from django.views.generic.edit import CreateView # type: ignore
from .models import Cat

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})


def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

# lesson pivots to class-based views

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # fields = ['name', 'breed', 'description', 'age']