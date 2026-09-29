from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hello/', views.hello, name='hello'),
    path('hello/<str:name>/', views.hello, name='hello_name'),
    path('greet/', views.greet_form, name='greet_form'),
]