from tasks.models import Task, User
from tasks.serializers import TaskSerializer, UserSerializers
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


# Class-based view for Task model
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can access
    filter_backends = [DjangoFilterBackend] # Enable filtering
    filterset_fields = ['priority', 'status'] # Enable filtering by priority and status
    ordering_fields = ['created_at', 'priority'] # Enable ordering by created_at and priority
    ordering = ['-created_at'] # Default ordering by created_at descending
    
    # Assign the task to the logged-in user
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    # Limit queryset to tasks of the logged-in user
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    

# Class-based view for User Registration
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializers(data = request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data)
    
    
# Class-based view for User Login
class LoginView(APIView):
    def post(self, request):
        # Get username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')
        # Find user by username
        user = User.objects.filter(username=username).first()
        
        # Check if user exists
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')
        
        return Response({
            'message': 'success'
        })