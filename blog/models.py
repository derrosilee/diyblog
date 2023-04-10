from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date


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


class Blog(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    # Foreign Key used because Blog can only have one author/User, but bloggers can have multiple blog posts.
    description = models.TextField(max_length=2000, help_text="Enter Your Blog Text Here")
    post_date = models.DateField(default=date.today)

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog instance.:
        """
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

