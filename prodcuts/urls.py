from django.urls import path
from prodcuts import views

urlpatterns = [
    path("",views.index,name = 'home'),
    path('about',views.about,name='about'),
    path("services",views.services,name='service'),
    path("contact",views.contact,name='contact'),
]