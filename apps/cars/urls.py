from apps.cars.views import Cars_list, new_car
from django.urls import path, include
urlpatterns = [
  
    path('',Cars_list, name='index'),
    path('new/',new_car,name='new')
]