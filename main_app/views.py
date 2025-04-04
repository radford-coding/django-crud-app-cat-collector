from django.shortcuts import render, redirect  # type: ignore
# from django.http import HttpResponse # type: ignore
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # type: ignore
from django.views.generic import ListView, DetailView  # type: ignore
from django.contrib.auth.views import LoginView # type: ignore
from .models import Cat, Toy
from .forms import FeedingForm

# Create your views here.

# old function-based homepage view
# def home(request):
#     return render(request, 'home.html')

# new CBV homepage
class Home(LoginView):
    template_name = 'home.html'


def about(request):
    return render(request, 'about.html')


def cat_index(request):
    cats = Cat.objects.all().order_by('name')
    return render(request, 'cats/index.html', {'cats': cats})


def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    # toys = Toy.objects.all()
    toys_not_associated = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
    feeding_form = FeedingForm()  # instantiate FeedingForm for rendering
    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'toys': toys_not_associated,
    })

# lesson pivots to class-based views


class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    # success_url = '/cats/' # unnecessary once the Cat model has a get_absolute_url method

    # this inherited method is called when a valid cat form is submitted
    def form_valid(self, form):
        form.instance.user = self.request.user # aka cat.user = self.request.user
        return super().form_valid(form) # calls inherited method, plus the behavior we defined on the previous line - not recursive


class CatUpdate(UpdateView):
    model = Cat
    # disallows renaming by excluding it
    fields = ['breed', 'description', 'age']


class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'  # need to redirect since that cat won't exist anymore

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False) # returns in-memory model object
        new_feeding.cat_id = cat_id # assign cat_id
        new_feeding.save() # save to database
    return redirect('cat-detail', cat_id=cat_id)

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def associate_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)

def remove_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.remove(toy_id)
    return redirect('cat-detail', cat_id=cat_id)