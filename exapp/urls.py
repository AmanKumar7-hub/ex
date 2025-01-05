from django.urls import path
from . import views

urlpatterns=[
    path('add', views.addTask, name='add'),
    path('task/<int:id>', views.getTask, name='singleTask'),
    path('tasks', views.getAllTask, name='tasks'),
    path('update/<int:id>', views.updateTask, name='update'),
    path('delete/<int:id>', views.deleteTask, name='delete')
]