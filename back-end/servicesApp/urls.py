from django.urls import path
from .views import *
urlpatterns = [
    path('', getAllServices, name="getAllServicesRoute"),
    path('add/', addService, name="addServicesRoute"),
    path('search/', getServiceByQuery, name="searchServiceRoute")
]