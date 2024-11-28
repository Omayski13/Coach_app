from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView, UpdateView, DeleteView

from coach_app.listings.forms import ListingCreateForm, ListingDetailForm, ListingEditForm, ListingDeleteForm
from coach_app.listings.models import Listing


# Create your views here.


class ListingCreateView(LoginRequiredMixin,CreateView):
    template_name = 'listings/listing-create.html'
    form_class = ListingCreateForm
    success_url = reverse_lazy('listing-dashboard')

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.author = self.request.user
        return super().form_valid(form)


class ListingDashboardView(LoginRequiredMixin,ListView):
    template_name = 'listings/listings-dashboard.html'
    queryset = Listing.objects.all().order_by('-created_at')
    context_object_name = 'listings'


class ListingDetailView(LoginRequiredMixin,DetailView,FormView):
    template_name = 'listings/listing-details.html'
    model = Listing
    form_class = ListingDetailForm

    def get_initial(self):
        return self.object.__dict__


class ListingEditView(LoginRequiredMixin,UpdateView):
    template_name = 'listings/listings-edit.html'
    form_class = ListingEditForm
    model = Listing
    success_url = reverse_lazy('listing-dashboard')


class ListingDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'listings/listings-delete.html'
    form_class = ListingDeleteForm
    model = Listing
    success_url = reverse_lazy('listing-dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


