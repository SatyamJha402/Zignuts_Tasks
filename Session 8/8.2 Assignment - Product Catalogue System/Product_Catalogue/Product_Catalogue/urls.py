from django.contrib import admin
from django.urls import path, include

# urlpatterns for the project
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('products.urls'))
]