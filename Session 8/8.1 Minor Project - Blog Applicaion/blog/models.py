from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Model representing a blog post
class Post(models.Model):
    # Post title (max length = 100), body of the post, date posted (set to current time), and author
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Returns post title when the object is printed in admin panel
    def __str__(self):
        return self.title
    
    # get the URL to view the post detail
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    