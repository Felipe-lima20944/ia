# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('responder/', views.responder, name='responder'),
    path('conversas/', views.listar_conversas, name='listar_conversas'),
    path('conversas/<uuid:conversa_id>/', views.carregar_conversa, name='carregar_conversa'),
    path('conversas/<uuid:conversa_id>/excluir/', views.excluir_conversa, name='excluir_conversa'),
]