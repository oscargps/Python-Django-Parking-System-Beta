from apps.owners.views import Owners
from django.urls import path, include
urlpatterns = [
    
    path('', Owners),
]