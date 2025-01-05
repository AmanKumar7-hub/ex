from django.db import models

STATUS_CHOICES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
        ('pending', 'Peding'),
]

# Create your models here.
class TaskModel(models.Model):
    title =models.CharField(max_length=100)
    description =models.CharField(max_length=200)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='incomplete',
    )

    def __str__(self):
        return self.title