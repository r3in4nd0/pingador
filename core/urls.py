from django.urls import path
from . import views

urlpatterns = [
    path('pingar/<ip>',views.pingar),
    path('poc', views.blogs),
    path('',views.home),
]