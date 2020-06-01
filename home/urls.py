from . import views
from django.urls import path, include



urlpatterns = [
    path('',views.index, name='index'),
    path('contact', views.contact,name='contact'),
    path('about', views.Members, name='portfolio'),
]

