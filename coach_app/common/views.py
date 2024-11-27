from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView

from coach_app.common.models import Like
from coach_app.drills.models import Drill


# Create your views here.


class HomePageView(DetailView):
    template_name = 'home-page.html'
    context_object_name = 'drill'

    def get_object(self):
        drill = Drill.objects.filter(approved=True, graphics__isnull=False).first()
        return drill




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

    return redirect(request.META.get('HTTP_REFERER') + f'#{drill_pk}')
