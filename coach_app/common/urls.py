from django.urls import path

from coach_app.common.views import HomePageView, likes_functionality, add_drill_to_favourites

urlpatterns = [
    path('', HomePageView.as_view(),name='home-page'),
    path('like/<int:drill_pk>', likes_functionality, name='like'),
    path('favourite/<int:drill_pk>', add_drill_to_favourites, name='add-favourites'),
]
