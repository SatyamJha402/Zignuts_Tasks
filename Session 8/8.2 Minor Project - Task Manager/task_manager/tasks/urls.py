from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tasks import views
from .views import RegisterView, LoginView

# Setting up router for TaskViewSet
router = DefaultRouter()
router.register(r'tasks',views.TaskViewSet, basename='task')

# Defining URL patterns
urlpatterns = [
    path("", include(router.urls)),
    path('api_auth', include('rest_framework.urls')), # For browsable API login/logout
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view())    
]
