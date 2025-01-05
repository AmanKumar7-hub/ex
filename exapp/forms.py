from django import forms
from .models import TaskModel

# Creating forms with the help of task model instead of using single field 
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel # this will capture fields from task model 
        fields ="__all__"  # specifies what fields need to create form