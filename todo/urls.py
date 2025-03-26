from django.urls import path
from . import views


urlpatterns = [
  path('cadastrar_tarefas/', views.cadastrar_tarefas, name='cadastrar_tarefas'),
  path('listar_tarefas/', views.listar_tarefas, name='listar_tarefas'),
  path('deletar_tarefa/<int:id>', views.deletar_tarefa, name='deletar_tarefa' )
] 