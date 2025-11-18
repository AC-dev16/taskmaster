from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    # Get uncompleted tasks ordered by due date (earliest first)
    todo_tasks = Task.objects.filter(completed=False).order_by('due_date')
    
    # Get completed tasks
    done_tasks = Task.objects.filter(completed=True).order_by('due_date')
    
    context = {
        'todo_tasks': todo_tasks,
        'done_tasks': done_tasks,
    }
    
    return render(request, 'tasks/index.html', context)
