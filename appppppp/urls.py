from django.urls import path
from .views import index
from .views import index1
from .views import index2

urlpatterns = [
    path('index',index),
    path('index1',index1),
    path('index3',index3),

]
