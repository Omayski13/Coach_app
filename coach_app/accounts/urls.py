


from django.urls import path, include

from coach_app.accounts.views import UserRegisterVIew

urlpatterns = [
    path('register/', UserRegisterVIew.as_view(),name='user-register'),
]