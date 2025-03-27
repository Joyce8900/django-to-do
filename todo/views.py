from django.shortcuts import get_object_or_404, render,redirect
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














# def concluir_tarefa(request):
#   todo = request.Post.get('completed')
#   if (todo):
#     todo.completed = True
#     todo.save()
  


