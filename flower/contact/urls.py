from django.urls import path
from . import views
from .views import *

urlpatterns=[
   #     path('', views.contact, name='contact'),
   # path('', Contact, name='contact1'),
   path('', views.Contact, name='contact'),
]