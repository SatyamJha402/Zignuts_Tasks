from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
    # path('tasks/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('tasks/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
