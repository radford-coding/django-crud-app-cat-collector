from django.shortcuts import render # type: ignore
# from django.http import HttpResponse # type: ignore
from django.views.generic.edit import CreateView, UpdateView, DeleteView # type: ignore
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
    # fields = ['name', 'breed', 'description', 'age'] # other option for only showing certain model fields in the form
    # success_url = '/cats/' # unnecessary once the Cat model has a get_absolute_url method

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age'] # disallows renaming by excluding it

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/' # need to redirect since that cat won't exist anymore