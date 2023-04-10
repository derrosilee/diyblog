from django.shortcuts import render


# Create your views here.
# TODO:: Change to class list view for all the blogs
def index(request):
    return render(request, template_name='blog/index.html')
