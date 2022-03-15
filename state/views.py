from django.core.files import images
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import media

from .models import Category


# Create your views here.


def stateCategory(request, category_slug=None):
    categories = None
    states =None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        states = Category.objects.filter(category=categories)
    else:
        pass


    states = Category.objects.all()

    context ={
        'states': states,
        }
    return render(request, 'home.html', context)


