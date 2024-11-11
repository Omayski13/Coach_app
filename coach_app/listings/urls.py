from django.urls import path, include

from coach_app.common.views import HomePageView
from coach_app.listings.views import ListingCreateView, ListingDashboardView, ListingDetailView, ListingEditView, \
    ListingDeleteView

urlpatterns = [
    path('create/',ListingCreateView.as_view(), name='listing-create'),
    path('dashboard/',ListingDashboardView.as_view(), name='listing-dashboard'),
    path('<int:pk>/',include([
        path('details/', ListingDetailView.as_view(), name='listing-details'),
        path('edit/', ListingEditView.as_view(), name='listing-edit'),
        path('delete/', ListingDeleteView.as_view(), name='listing-delete'),
    ])),
]
