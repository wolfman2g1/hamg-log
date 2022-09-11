from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='test'),
    path('', views.list_all_contacts, name='index'),
    path('new/', views.create_contact, name='contact_create')
]