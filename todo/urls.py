from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
  path('todo/cadastrar_tarefas', views.cadastrar_tarefas, name='cadastrar_tarefas'),
]