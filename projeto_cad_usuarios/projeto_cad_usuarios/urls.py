from app_cad_usuarios import views 
from django.urls import path

urlpatterns = [
    # rota, view responsável, nome de referência
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
