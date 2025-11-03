from rest_framework import serializers
from tasks.models import Task, PRIORITY_CHOICES, STATUS_CHOICES
from django.contrib.auth.models import User


# Serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username') # Read-only field to show username of the task owner
    
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'due_date', 'priority', 'status']

# Serializer for User model
class UserSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
        extra_kwargs = {'password': {'write_only':True}} # Make password write-only
        
    # Override create method to hash password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user