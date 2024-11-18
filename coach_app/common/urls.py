from django.urls import path

from coach_app.common.views import HomePageView, likes_functionality

urlpatterns = [
    path('', HomePageView.as_view(),name='home-page'),
    path('like/<int:drill_pk>', likes_functionality, name='like'),
]
