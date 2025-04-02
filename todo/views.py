from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Todo
from django.utils import timezone
from datetime import datetime


def listar_tarefas(request):
  todos = Todo.objects.all()
  context = {
    'todos': todos,
    'now': timezone.now().date()
  }
  return render(request, 'listar_tarefas.html', context)

# Create your views here.
def cadastrar_tarefas(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    description = request.POST.get('description')
    completed_at = request.POST.get('completed_at')
    todo =Todo(title=title, description=description, completed_at = completed_at)
    todo.save()

    print(todo.completed_at)
    return redirect('listar_tarefas')
  return render(request, 'cadastrar_tarefas.html')



def deletar_tarefa(request,id):
  todo = Todo.objects.filter(pk=id).delete()
  return redirect('listar_tarefas')


def completar_tarefa(request, id):
    if request.method == 'POST':
      todo = get_object_or_404(Todo, pk=id)
      todo.completed = True
      todo.save()
      
    print(todo.completed)
    return redirect('listar_tarefas')

def editar_tarefa(request, id):
  tarefa_obj = get_object_or_404(Todo, id=id)
  if request.method == 'POST':
    tarefa_obj.title = request.POST.get('title')
    tarefa_obj.description = request.POST.get('description')
    tarefa_obj.completed_at = request.POST.get('completed_at') 
    tarefa_obj.completed = False
    tarefa_obj.updated_at = timezone.now()
    
    tarefa_obj.save()
    return redirect('listar_tarefas')

  
  tarefa = {
        'id': tarefa_obj.id,
        'title': tarefa_obj.title,
        'description': tarefa_obj.description,
        'completed_at': tarefa_obj.completed_at.strftime('%Y-%m-%d') if tarefa_obj.completed_at else '',            
  }
    
  return render(request, 'editar_tarefa.html', {'tarefa': tarefa})  










  


