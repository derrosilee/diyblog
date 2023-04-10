from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class BlogAuthor(models.Model):
    """
    Model Representing a Blogger
    """
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter Your Bio Details Here")
    author_avatar = models.ImageField(upload_to='author-avatar')

    class Meta:
        ordering = ["user", "bio", "author_avatar"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog-author instance.
        """
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the model object
        """
        return self.user.username
