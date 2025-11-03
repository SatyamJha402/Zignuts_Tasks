from rest_framework import serializers
from tasks.models import Task, PRIORITY_CHOICES, STATUS_CHOICES
from django.contrib.auth.models import User


# Serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'due_date', 'priority', 'status'] # All fields of Task model

# Serializer for User model
class UserSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password'] # All fields of User model
        
        extra_kwargs = {'password': {'write_only':True}} # Password should be write-only
        
    # Create method to handle user creation
    def create(self, validated_data):
        # Create a new user with hashed password
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password) 
        user.save()
        return user