from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()  # Get all tasks
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)  # Create a new task
            return redirect('task_list')  # Redirect to the task list page
    return render(request, 'todo/add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()  # Delete the task
    return redirect('task_list')  # Redirect to the task list page
