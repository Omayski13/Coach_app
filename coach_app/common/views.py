from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from coach_app.common.models import Like


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home-page.html'


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
    # return reverse_lazy('drill-details')