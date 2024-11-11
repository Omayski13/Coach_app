from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from coach_app.accounts.forms import AppUserLoginForm
from coach_app.accounts.views import UserRegisterVIew, UserDetailsView, UserEditView

urlpatterns = [
    path('register/', UserRegisterVIew.as_view(),name='user-register'),
    path('login/', LoginView.as_view(authentication_form=AppUserLoginForm),name='user-login'),
    path('logout/', LogoutView.as_view(),name='user-logout'),
    path('profile/<int:pk>/', include([
        path('details/', UserDetailsView.as_view(), name='user-details'),
        path('edit/', UserEditView.as_view(), name='user-edit'),
    ]))
]