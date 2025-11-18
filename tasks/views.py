from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    # Get uncompleted tasks ordered by due date (earliest first)
    todo_tasks = Task.objects.filter(completed=False).order_by('due_date')
    
    # Get completed tasks
    done_tasks = Task.objects.filter(completed=True).order_by('due_date')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm()
    
    context = {
        'todo_tasks': todo_tasks,
        'done_tasks': done_tasks,
        'form': form,
    }
    
    return render(request, 'tasks/index.html', context)
