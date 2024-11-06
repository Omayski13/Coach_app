from django.urls import path

from coach_app.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(),name='home-page'),
]
