from django.urls import path
from . import views

urlpatterns = [
    path('pingar/<ip>',views.pingar),
    path('',views.home),
]