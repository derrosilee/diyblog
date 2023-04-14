from . import views
from django.urls import path


urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail')
]

urlpatterns +=[
    path('bloggers/', views.BlogAuthorListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>/', views.BlogListByAuthorView.as_view(), name='blogs-by-author')
]
