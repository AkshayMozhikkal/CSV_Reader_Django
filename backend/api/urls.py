from django.urls import path, include
from .views import *

urlpatterns = [
   path('', home, name='home'),
   path('result/', result, name='result'),
   path('bits/', CsvReader.as_view(), name='bits') 
]
