from django.contrib import messages
from django.contrib.auth import login, views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *


class ChangePassword(views.PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'registration/password_change_form.html'


class ResetPassword(views.PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'registration/password_reset_form.html'


class ResetPasswordConfirm(views.PasswordResetConfirmView):
    form_class = UserPasswordConfirmForm
    template_name = 'registration/password_reset_confirm.html'


class RegisterView(views.FormView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        profile = Profile.objects.create(user=user)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        else:
            messages.error(request, 'Ошибка валидации')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'registration/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
