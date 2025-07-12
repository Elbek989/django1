from django.urls import path
from .views import json_qaytar
urlpatterns =[
    path('salom/',json_qaytar),
]