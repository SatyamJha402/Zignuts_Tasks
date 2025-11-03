from django.urls import include, path
from rest_framework.routers import DefaultRouter
from products import views

# Using DefaultRouter to automatically create URL routes for the ProductViewSet
router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')

urlpatterns = [
    # Including the router-generated URLs
    path('', include(router.urls)),
]
