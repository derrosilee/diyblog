from . import views
from django.urls import path


urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail')
]