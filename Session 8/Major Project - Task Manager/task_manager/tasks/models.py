from django.db import models
from django.contrib.auth.models import User


PRIORITY_CHOICES = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low')
]

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed')
]

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks',null=False)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True, max_length=500)
    due_date = models.DateTimeField(blank=True, null = True)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10, default='medium', blank=True)
    status = models.CharField(default = 'pending', max_length=20)
    
    def __str__(self):
        return f"{self.title} [Completed: {self.status}]"
