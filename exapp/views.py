from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import TaskForm
from .models import TaskModel

# addTask function will add task to the inbuild database sqlite
def addTask(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            #return response if task is successfully added 
            return JsonResponse({'message': 'Task added successfully!', 'status': 'success'}, status=200) 
        # return json response if error occured during the invalid data 
        return JsonResponse({'message': 'Invalid data provided.', 'errors': task.errors, 'status': 'error'}, status=400)
    else:
        # this will create a form to add task 
        task = TaskForm()
    # return to the page with displaying template addForm.html at the add task
    return render(request, 'addForm.html', {'task': task})

#get single task by id  or will show individual task 
def getTask(request, id):
    task = get_object_or_404(TaskModel, id=id) # get object or will return not available task
    return render(request, 'singleTask.html', {'task': task})

# get all tasks available at the database 
def getAllTask(request):
    tasks = TaskModel.objects.all()
    return render(request, 'allTasks.html', {'tasks': tasks})

# delete task by using id as identifier
def deleteTask(request, id):
    task = get_object_or_404(TaskModel, id=id)
    if request.method == 'POST':
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully!', 'status': 'success'}, status=200)
    return JsonResponse({'message': 'Invalid request method.', 'status': 'error'}, status=405)


# it will update the task according to the id or specific task according to the id
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
