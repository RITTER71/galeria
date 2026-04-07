from django.urls import path
from .views import galeria

urlpatterns = [
    path('', galeria, name='galeria'),
]
