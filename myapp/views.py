from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home(request):
    my_list = [1,2,3,4,5]
    context = {'my_list': my_list}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
