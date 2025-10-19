from tasks.models import Task, User
from tasks.serializers import TaskSerializer, UserSerializers
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['priority', 'status']
    ordering_fields = ['created_at', 'priority']
    ordering = ['-created_at']
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
            
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializers(data = request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    
    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password!')
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'message': 'success',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username
        })