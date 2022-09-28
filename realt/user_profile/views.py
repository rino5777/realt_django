from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth import  logout
from .models import User
from .form import RegisterUserForm, LoginForm, ChangeUserInfoForm, ChangePass
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.




#----------------------------------------------------
class Logining(LoginView):
    template_name = 'user-profile/signin.html'
    form_class = LoginForm

def logoutuser(request):
    logout(request)
    return redirect('user_profile:login')


class RegisterUserView(CreateView):
    model = User
    template_name = 'user-profile/signup.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('user_profile:login')


class UserProfile(TemplateView):
    template_name = 'user-profile/agent-profile.html' 
    

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin,  UpdateView):
    model = User
    template_name = 'user-profile/agent-profile.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('user_profile:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class PassChange(SuccessMessageMixin,PasswordChangeView, LoginRequiredMixin):
    template_name = 'user-profile/change-password.html'
    success_message = 'Пароль пользователя изменен'
    form_class = ChangePass
    success_url = reverse_lazy('main:login')
    