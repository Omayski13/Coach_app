from django.urls import path, include

from coach_app.drills.views import DrillCreateView, DrillDashboardView, DrillDeleteView

urlpatterns = [
    path('create/',DrillCreateView.as_view(), name='drill-create'),
    path('dashboard/',DrillDashboardView.as_view(), name='drill-dashboard'),
    path('<int:pk>/',include([
    #     path('details/', ListingDetailView.as_view(), name='listing-details'),
    #     path('edit/', ListingEditView.as_view(), name='listing-edit'),
        path('delete/', DrillDeleteView.as_view(), name='drill-delete'),
    ])),
]
