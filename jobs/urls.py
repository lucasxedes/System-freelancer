from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('encotrar_jobs/', views.encontrar_jobs, name="encontrar_jobs"),
    path('aceitar_job/<int:id>/', views.aceitar_job, name="aceitar_job"),
    path('perfil/', views.perfil, name="perfil"),
    path('enviar_projeto/', views.enviar_projeto, name="enviar_projeto"),
]
