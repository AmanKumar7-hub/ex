from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import TaskForm
from .models import TaskModel

def addTask(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return JsonResponse({'message': 'Task added successfully!', 'status': 'success'}, status=200)
        return JsonResponse({'message': 'Invalid data provided.', 'errors': task.errors, 'status': 'error'}, status=400)
    else:
        task = TaskForm()
    return render(request, 'addForm.html', {'task': task})

def getTask(request, id):
    task = get_object_or_404(TaskModel, id=id)
    return render(request, 'singleTask.html', {'task': task})

def getAllTask(request):
    tasks = TaskModel.objects.all()
    return render(request, 'allTasks.html', {'tasks': tasks})

def deleteTask(request, id):
    task = get_object_or_404(TaskModel, id=id)
    if request.method == 'POST':
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully!', 'status': 'success'}, status=200)
    return JsonResponse({'message': 'Invalid request method.', 'status': 'error'}, status=405)

def updateTask(request, id):
    singleTask = get_object_or_404(TaskModel, id=id)
    if request.method == 'POST':
        task = TaskForm(request.POST, instance=singleTask)
        if task.is_valid():
            task.save()
            return JsonResponse({'message': 'Task updated successfully!', 'status': 'success'}, status=200)
        return JsonResponse({'message': 'Invalid data provided.', 'status': 'error'}, status=400)
    else:
        task = TaskForm(instance=singleTask)
    return render(request, 'updateTask.html', {'task': task})
