from django.contrib import admin
from .models import Blog, BlogAuthor, BlogCategory
# Register your models here.


admin.site.register(Blog)

admin.site.register(BlogAuthor)

admin.site.register(BlogCategory)