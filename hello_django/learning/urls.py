from django.urls import path, include
from learning import views

urlpatterns = [
    path('', views.index, name="index"),
]
