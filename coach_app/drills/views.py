from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from coach_app.drills.forms import DrillCreateFrom


# Create your views here.


class DrillCreateView(CreateView):
    template_name = 'drills/drills-create.html'
    form_class = DrillCreateFrom
    success_url = reverse_lazy('listing-dashboard')

    def form_valid(self, form):
        drill = form.save(commit=False)
        drill.author = self.request.user
        return super().form_valid(form)



