from django.urls import path
from .views import create_employee,create_departament,create_room,create_bemor

urlpatterns =[
    path('create-employee/', create_employee),
    path('create-departament/', create_departament),
    path('create-room/', create_room),
    path('create-bemor/', create_bemor),
    ]