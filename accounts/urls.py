from django.contrib.auth.views import *
from django.urls import path

from accounts.views import *

urlpatterns = [
    path('edit/', edit, name='edit'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),

    path('password_change/', ChangePassword.as_view(), name='password_change'),
    path('password_reset/', ResetPassword.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='password_reset_confirm'),

    path('password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='accounts/password_change_done.html'),
        name='password_change_done'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(
                template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
