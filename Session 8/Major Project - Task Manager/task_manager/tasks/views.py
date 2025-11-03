from tasks.models import Task, User
from tasks.serializers import TaskSerializer, UserSerializers
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


# Class based view for Task model
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can access
    filter_backends = [DjangoFilterBackend] # Enable filtering
    filterset_fields = ['priority', 'status'] # Fields to filter by
    ordering_fields = ['created_at', 'priority'] # Fields to order by
    ordering = ['-created_at'] # Default ordering
    
    # Override perform_create to associate task with the logged-in user
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    # Override get_queryset to return tasks only for the logged-in user
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    

# Class based view for User Registration
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny] # Allow any user to access this view
    def post(self, request):
        # Create a new user
        serializer = UserSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        
        # Return user data along with JWT tokens
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    
    
# Class based view for User Login
class LoginView(APIView):
    permission_classes = [permissions.AllowAny] # Allow any user to access this view
    
    def post(self, request):
        # Authenticate user and return JWT tokens
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first()
        
        # Handle authentication failures
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')
        
        refresh = RefreshToken.for_user(user) # Generate JWT tokens
        
        # Return tokens and username
        return Response({
            'message': 'success',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username
        })