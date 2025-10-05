from django.urls import include, path
from rest_framework.routers import DefaultRouter
from products import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
