
from django.urls import path
from . import views

app_name = 'bigdoc'

urlpatterns = [
    path('', views.index, name='index')
]
