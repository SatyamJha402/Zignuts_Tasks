from rest_framework import serializers
from tasks.models import Task, PRIORITY_CHOICES, STATUS_CHOICES
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'due_date', 'priority', 'status']
        

