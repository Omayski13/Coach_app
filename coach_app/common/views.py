from urllib.parse import urlparse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView
from rest_framework.exceptions import PermissionDenied

from coach_app.common.models import Like, FavoriteDrill
from coach_app.drills.models import Drill


# Create your views here.


class HomePageView(DetailView):
    # template_name = 'common/home-page-not-logged.html'
    context_object_name = 'drill'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['drills'] = Drill.objects.filter(approved=True)

        return context

    def get_object(self):
        drill = Drill.objects.filter(approved=True, graphics__isnull=False).last()
        return drill


    def get_template_names(self):
        if self.request.user.is_authenticated:
            return['common/home-page-logged.html']
        else:
            return ['common/home-page-not-logged.html']


@login_required
def add_drill_to_favourites(request,drill_pk: int):

    favourite_drill = FavoriteDrill.objects.filter(
        to_drill_id=drill_pk,
        user=request.user
    ).first()

    if favourite_drill:
        favourite_drill.delete()
    else:
        favourite_drill = FavoriteDrill(to_drill_id=drill_pk,user=request.user)
        favourite_drill.save()

    referer = request.META.get('HTTP_REFERER')

    if referer:
        parsed_url = urlparse(referer)
        if 'details' in parsed_url.path:
            return redirect(reverse('drill-details', args=[drill_pk]))
        elif 'favourites' in parsed_url.path:
            return redirect(f"{reverse('user-favourites', args=[request.user.pk])}#{drill_pk}")
        elif 'dashboard' in parsed_url.path:
            redirect(f"{reverse('drill-dashboard')}#{drill_pk}")

    return redirect(f"{reverse('user-drills', args=[request.user.pk])}#{drill_pk}")


@login_required
def likes_functionality(request, drill_pk: int):
    liked_object = Like.objects.filter(
        to_drill_id=drill_pk,
        user=request.user
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_drill_id=drill_pk, user=request.user)
        like.save()

    referer = request.META.get('HTTP_REFERER')

    if referer:
        parsed_url = urlparse(referer)
        if 'details' in parsed_url.path:
            return redirect(reverse('drill-details', args=[drill_pk]))
        elif 'favourites' in parsed_url.path:
            return redirect(f"{reverse('user-favourites', args=[request.user.pk])}#{drill_pk}")
        elif 'dashboard' in parsed_url.path:
            redirect(f"{reverse('drill-dashboard')}#{drill_pk}")

    return redirect(f"{reverse('user-drills', args=[request.user.pk])}#{drill_pk}")

@login_required
def approve_drill(request, pk):
    if request.user.has_perm('drills.can_approve_drills'):
        drill = get_object_or_404(Drill, pk=pk)
        drill.approved = True
        drill.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        raise PermissionDenied
