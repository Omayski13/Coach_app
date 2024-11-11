from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView

from coach_app.listings.forms import ListingCreateForm, ListingDetailForm
from coach_app.listings.models import Listing


# Create your views here.


class ListingCreateView(CreateView):
    template_name = 'listings/listing-create.html'
    form_class = ListingCreateForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.author = self.request.user
        return super().form_valid(form)


class ListingDashboardView(ListView):
    template_name = 'listings/listings-dashboard.html'
    queryset = Listing.objects.all()
    context_object_name = 'listings'


class ListingDetailView(DetailView,FormView):
    template_name = 'listings/listing-details.html'
    model = Listing
    form_class = ListingDetailForm
    
    def get_initial(self):
        return self.object.__dict__


