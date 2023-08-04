from django.urls import path

from . import views

urlpatterns = [
    #ex: /companies/
    path("", views.index, name="index"),
    #ex: /companies/blackrock
    path("<str:company>/", views.company, name="company"),
]