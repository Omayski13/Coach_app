from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from coach_app.accounts.forms import CustomLoginForm
from coach_app.accounts.views import UserRegisterVIew

urlpatterns = [
    path('register/', UserRegisterVIew.as_view(),name='user-register'),
    path('login/', LoginView.as_view(authentication_form=CustomLoginForm),name='user-login'),
    path('logout/', LogoutView.as_view(),name='user-logout'),
]