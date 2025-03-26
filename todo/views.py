from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def cadastrar_tarefas(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    description = request.POST.get('description')
    todo =Todo(title=title, description=description)
    todo.save()
  return render(request, 'cadastrar_tarefas.html')