from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from coach_app.drills.forms import DrillCreateForm, DrillDeleteForm, DrillEditForm
from coach_app.drills.models import Drill


# Create your views here.


class DrillCreateView(CreateView):
    template_name = 'drills/drills-create.html'
    form_class = DrillCreateForm
    success_url = reverse_lazy('drill-dashboard')

    def form_valid(self, form):
        drill = form.save(commit=False)
        drill.author = self.request.user
        return super().form_valid(form)


class DrillDashboardView(ListView):
    template_name = 'drills/drills-dashboard.html'
    context_object_name = 'drills'

    def get_queryset(self):
        queryset = Drill.objects.all()

        # Get query parameters
        for_age_group = self.request.GET.get('for_age_group')
        focus = self.request.GET.get('focus')

        # Apply filters
        if for_age_group:
            queryset = queryset.filter(for_age_group=for_age_group)
        if focus:
            queryset = queryset.filter(focus=focus)

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query_params = self.request.GET.dict()

        valid_filters = {}
        if 'age_group' in query_params:
            valid_filters['age_group'] = query_params['age_group']
        if 'focus' in query_params:
            valid_filters['focus'] = query_params['focus']

        context['clean_query_params'] = valid_filters
        return context


class DrillDeleteView(DeleteView):
    template_name = 'drills/drills-delete.html'
    form_class = DrillDeleteForm
    model = Drill
    success_url = reverse_lazy('drill-dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class DrillEditView(UpdateView):
    template_name = 'drills/drills-edit.html'
    form_class = DrillEditForm
    model = Drill
    success_url = reverse_lazy('drill-dashboard')








