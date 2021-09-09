from django.urls import path

from .views import *

urlpatterns = [ 
    path('contact/', contact, name='contact'),
    path('about/', about_us, name='about'),
    path('privacy_policy', privace_policy, name='privacy_policy'),
    path('order_history/', order_history, name='order_history'),
]