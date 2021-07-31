from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import *


def user_logout(request):
    logout(request)
    return render(request, 'accounts/logged_out.html')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно авторизовались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторизации')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {"form": form})


class ChangePassword(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'accounts/password_change_form.html'


class ResetPassword(PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'accounts/password_reset_form.html'


class ResetPasswordConfirm(PasswordResetConfirmView):
    form_class = UserPasswordConfirmForm
    template_name = 'accounts/password_reset_confirm.html'


