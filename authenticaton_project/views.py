from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy




def home(request):
    return render(request, 'base.html')

class signup(CreateView):
    model=User
    form_class=RegisterForm
    template_name = 'login.html'	
    success_url = reverse_lazy('homepage')

class loginView(LoginView):
    model = User
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')

def usrLogout(request):
    user=logout(request)
    return redirect('homepage')