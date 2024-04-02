from django.urls import path
from App.views import landingpage

urlpatterns = [
    path("home/",landingpage,name='landingpage'),
]