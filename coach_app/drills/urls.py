from django.urls import path, include

from coach_app.common.views import approve_drill
from coach_app.drills.views import DrillCreateView, DrillDashboardView, DrillDeleteView, DrillEditView, DrillDetailsView

urlpatterns = [
    path('create/',DrillCreateView.as_view(), name='drill-create'),
    path('dashboard/',DrillDashboardView.as_view(), name='drill-dashboard'),
    path('<int:pk>/',include([
        path('approve/',approve_drill, name='approve_drill'),
        path('details/', DrillDetailsView.as_view(), name='drill-details'),
        path('edit/', DrillEditView.as_view(), name='drill-edit'),
        path('delete/', DrillDeleteView.as_view(), name='drill-delete'),
    ])),
]
