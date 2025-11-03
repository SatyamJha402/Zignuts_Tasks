from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name = "blog-home"), # home page
    path('about/', views.about, name = "blog-about"), # about page
    path('register/', user_views.register, name='register'), # user registration
    path('profile/', user_views.profile, name='profile'), # user profile
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'), # user login
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'), # user logout
    path('post/<int:pk>/', PostDetailView.as_view(), name= 'post-detail'), # post detail view
    path('post/<int:pk>/update', PostUpdateView.as_view(), name= 'post-update'), # post update view
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name= 'post-delete'), # post delete view
    path('post/new/', PostCreateView.as_view(), name= 'post-create') # post create view
]