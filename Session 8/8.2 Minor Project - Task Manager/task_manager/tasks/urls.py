from django.urls import include, path
from rest_framework.routers import DefaultRouter
from tasks import views

router = DefaultRouter()
router.register(r'tasks',views.TaskViewSet, basename='task')

urlpatterns = [
    path("", include(router.urls)),
    path('api_auth', include('rest_framework.urls'))
]