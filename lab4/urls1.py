from django.urls import path

from lab4 import views1

app_name = 'lab4'

urlpatterns = [
    path(r'', views1.index, name='index'),
]
