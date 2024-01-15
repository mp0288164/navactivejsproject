from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
]