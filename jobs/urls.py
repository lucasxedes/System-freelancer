from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('encotrar_jobs/', views.encontrar_jobs, name="encontrar_jobs"),
]
