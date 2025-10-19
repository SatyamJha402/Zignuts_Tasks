from rest_framework import serializers
from tasks.models import Task, PRIORITY_CHOICES, STATUS_CHOICES
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'due_date', 'priority', 'status']

class UserSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
        extra_kwargs = {'password': {'write_only':True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user