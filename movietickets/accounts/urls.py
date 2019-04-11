from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include

from django.urls import path, re_path
from django.urls import reverse_lazy

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
    )
app_name='accounts'
urlpatterns=[
    url(r'^',include('home.urls'),name='home'),
    url(r'^login/$',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^logout/$',LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    url(r'^register/',views.register,name='register'),
    url(r'^register/reg_valid/$',views.register,name='reg_valid'),
    url(r'^profile/$',views.view_profile,name='view_profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^change_pwd/$',views.change_pwd,name='change_pwd'),

    url(r'reset_password/$',auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html',
    success_url='/accounts/password_reset/done/')),

    url(r'password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_done.html')),



   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_confirm.html'),
    name='password_reset_confirm'),


    url(r'password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html')),

]