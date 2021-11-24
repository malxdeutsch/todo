from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.

def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            task = Todo.objects.create(**form.cleaned_data)
            return redirect('tdlist')

    if request.method == 'GET':
        form = TodoForm()
    return render(request, 'add_task.html', {'form': form})


def display_todo(request):
    tdlist = Todo.objects.all()
    return render(request,'display_todo.html', {'tdlist':tdlist})