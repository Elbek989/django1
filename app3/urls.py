from django.urls import path
from . import views

urlpatterns = [
    path('aaa/', views.index),
    path('category/<int:pk>/', views.category, name='category'),
]
