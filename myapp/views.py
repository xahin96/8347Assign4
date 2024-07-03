from django.shortcuts import render
from django.views.generic import TemplateView

from myapp.models import Book


def index(request):
    booklist = Book.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index0.html', {'booklist': booklist})


def home(request):
    my_list = [1, 2, 3, 4, 5]
    context = {'my_list': my_list}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'myapp/about0.html')
