from django.shortcuts import render, redirect
from .models import Task


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {'tasks': tasks})


def create_tasks(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    print(request.POST)
    return redirect('/')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')