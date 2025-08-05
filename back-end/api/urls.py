from django.urls import path, include
urlpatterns = [
    path('users/', include('usersApp.urls')),
    path('services/', include('servicesApp.urls'))
]