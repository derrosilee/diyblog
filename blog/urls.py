from . import views
from django.urls import path


urlpatterns = [
    path('blogs/', views.BlogListView.as_view(), name='blogs')
]