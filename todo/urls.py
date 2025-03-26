from django.urls import path
from . import views


urlpatterns = [
  path('todo/cadastrar_tarefas/', views.cadastrar_tarefas, name='cadastrar_tarefas'),
  path('todo/listar_tarefas/', views.listar_tarefas, name='listar_tarefas'),

] 