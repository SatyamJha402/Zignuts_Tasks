from django.db import models
from django.contrib.auth.models import User

# Choices for priority
PRIORITY_CHOICES = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low')
]
# Choices for status
STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed')
]


# Task model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks') # Link task to a user
    title = models.CharField(max_length = 200) # Task title
    description = models.TextField(blank=True, max_length=500) # Task description
    due_date = models.DateTimeField(blank=True, null = True) # Due date
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10, default='medium', blank=True) # Task priority
    status = models.CharField(choices=STATUS_CHOICES, default = 'pending', max_length=15) # Task status
    
    def __str__(self):
        return f"{self.title} [Completed: {self.status}]"
