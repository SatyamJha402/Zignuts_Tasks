from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# view to render the home page with all blog posts
def home(request):
    context = {
        # Fetches all Post objects from the database
        "posts": Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# Class-based views for blog post operations
class PostListView(ListView):
    model = Post
    # Custom template
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # Ordering posts by newest first
    ordering = ['-date_posted']

# Class-based view for detailed view of a single post
class PostDetailView(DetailView):
    model = Post
    
# Class-based view for creating a new blog post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # Fields to be included in the form
    fields = ['title', 'content']
    
    # Assign the current user as the author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# Class-based view for updating an existing blog post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    # Check if the current user is the author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # access control to ensure only authors can update their posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

# Class-based view for deleting a blog post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'
    
    # access control to ensure only authors can delete their posts
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

# view to render the about page
def about(request):
    return render(request, 'blog/about.html', {"title": "About"})