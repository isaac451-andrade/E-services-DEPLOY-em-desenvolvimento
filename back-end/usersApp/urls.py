from django.urls import path
from .views import *
urlpatterns = [
    path('', getAllUsers, name='getAllUsersRoute'),
    path('add/', addUser, name="addUserRoute"),
    path('getBy/<int:id>/', getUserById, name="getUserByIdRoute"),
    path('getBy/<str:name>/', getUserByName, name="getUserByNameRoute"),
    path('delete/<int:id>/', deleteUserById, name='deleteUserByIdRoute'),

]
