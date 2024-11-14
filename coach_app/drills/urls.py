from django.urls import path, include

from coach_app.common.views import HomePageView
from coach_app.drills.views import DrillCreateView, DrillDashboardView
from coach_app.listings.views import ListingCreateView, ListingDashboardView, ListingDetailView, ListingEditView, \
    ListingDeleteView

urlpatterns = [
    path('create/',DrillCreateView.as_view(), name='drill-create'),
    path('dashboard/',DrillDashboardView.as_view(), name='drill-dashboard'),
    # path('<int:pk>/',include([
    #     path('details/', ListingDetailView.as_view(), name='listing-details'),
    #     path('edit/', ListingEditView.as_view(), name='listing-edit'),
    #     path('delete/', ListingDeleteView.as_view(), name='listing-delete'),
    # ])),
]
