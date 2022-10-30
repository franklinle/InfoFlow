from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="index"),
    path("sports", views.Sports, name="sports"),
    path("tech", views.Tech, name="tech"),
    path("business", views.Business, name="business"),
    path("science", views.Science, name="science"),
    path("entertainment", views.Entertainment, name="entertainment")   
    ]
