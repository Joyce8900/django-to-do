from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo

def listar_tarefas(request):
  todos = Todo.objects.all()
  return render(request, 'listar_tarefas.html', {'todos': todos})

# Create your views here.
def cadastrar_tarefas(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    description = request.POST.get('description')
    todo =Todo(title=title, description=description)
    todo.save()
    return redirect('listar_tarefas')
  return render(request, 'cadastrar_tarefas.html')
  


