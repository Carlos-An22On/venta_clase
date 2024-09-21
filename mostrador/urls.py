from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.mostrador_view, name='mostrador_view'),
]
