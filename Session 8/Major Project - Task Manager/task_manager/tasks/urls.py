from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tasks import views
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

# Define router and register TaskViewSet
router = DefaultRouter()
router.register(r'tasks',views.TaskViewSet, basename='task')

# Define URL patterns
urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()) # Endpoint to refresh JWT tokens
]
