from django.db import models
from django.contrib.auth.models import User

# Define choices for priority and status fields
PRIORITY_CHOICES = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low')
]

#   Define choices for status field
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed')
]

# Model for Task
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks',null=False) # Link task to a user
    title = models.CharField(max_length = 200) 
    description = models.TextField(blank=True, max_length=500)
    due_date = models.DateTimeField(blank=True, null = True) # Optional due date
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10, default='medium', blank=True) # Priority with default value as medium
    status = models.CharField(choices= STATUS_CHOICES, default = 'pending', max_length=20) # Status with default value as pending
    
    def __str__(self):
        return f"{self.title} [Completed: {self.status}]"
