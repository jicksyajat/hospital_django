from django.urls import path,include
from .views import *
urlpatterns = [
    path('',register_view,name='register'),    
    path('home',home,name='home'),
    path('doctors',doctor,name='doctors'),
    path('depts',department,name='depts'),
    path('booking',bookingss,name='booking'),
]