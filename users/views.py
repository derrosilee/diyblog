from django.shortcuts import render
from .forms import RegisterForm


# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm
        return render(request, 'registration/register.html', {'form': form})
