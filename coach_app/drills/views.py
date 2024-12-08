from cloudinary.uploader import destroy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, FormView

from coach_app.comments.forms import CommentAddForm
from coach_app.drills.forms import DrillCreateForm, DrillDeleteForm, DrillEditForm, SearchForm
from coach_app.drills.models import Drill


# Create your views here.


class DrillCreateView(LoginRequiredMixin, CreateView):
    template_name = 'drills/drills-create.html'
    form_class = DrillCreateForm
    success_url = reverse_lazy('drill-dashboard')

    def form_valid(self, form):
        drill = form.save(commit=False)
        drill.author = self.request.user
        return super().form_valid(form)


class DrillDashboardView(LoginRequiredMixin, ListView, FormView):
    template_name = 'drills/drills-dashboard.html'
    context_object_name = 'drills'
    paginate_by = 5
    form_class = SearchForm

    def get_queryset(self):
        queryset = Drill.objects.all()

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = queryset.filter(name__icontains=query)

        for_age_group = self.request.GET.get('for_age_group')
        focus = self.request.GET.get('focus')
        approved = self.request.GET.get('approved')

        if for_age_group:
            queryset = queryset.filter(for_age_group=for_age_group)
        if focus:
            queryset = queryset.filter(focus=focus)
        if approved == 'True':
            queryset = queryset.filter(approved=True)

        order_by = self.request.GET.get('order_by', '-created_at')
        if order_by == 'likes':
            queryset = queryset.annotate(like_count=Count('likes')).order_by('-like_count', '-created_at')
        elif order_by == '-likes':
            queryset = queryset.annotate(like_count=Count('likes')).order_by('like_count', '-created_at')
        elif order_by == 'comments':
            queryset = queryset.annotate(comment_count=Count('comments')).order_by('-comment_count', '-created_at')
        elif order_by == '-comments':
            queryset = queryset.annotate(comment_count=Count('comments')).order_by('comment_count', '-created_at')
        else:
            queryset = queryset.order_by(order_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_drills_count'] = Drill.objects.count()
        context['age_groups'] = ['U5 - U6', 'U7 - U8', 'U9 - U10', 'U11 - U12', 'U13 - U14', 'U15 - U16', 'U17 - U19']
        context['focus_options'] = ['Удари', 'Подаване', 'Дрибъл', '1 срещу 1', '2 срещу 1']

        for drill in context['drills']:
            drill.has_liked = drill.likes.filter(user=self.request.user).exists()

        return context


class DrillDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'drills/drills-details.html'
    model = Drill

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = CommentAddForm()
        context['comments'] = self.object.comments.all()
        context['likes'] = self.object.likes.all()
        self.object.has_liked = self.object.likes.filter(user=self.request.user).exists()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentAddForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_drill_id = self.object.id
            comment.author = request.user
            comment.save()

            return redirect(f'{self.request.path}#comments')


class DrillEditView(LoginRequiredMixin, UpdateView):
    template_name = 'drills/drills-edit.html'
    form_class = DrillEditForm
    model = Drill
    success_url = reverse_lazy('drill-dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user != self.object.author:
            if not self.request.user.is_superuser:
                raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        old_graphics = self.get_object().graphics
        response = super().form_valid(form)

        new_graphics = self.object.graphics
        if old_graphics != new_graphics and old_graphics:
            try:
                public_id = old_graphics.public_id
                destroy(public_id)
            except Exception as e:
                print(f"Error deleting old graphics from Cloudinary: {e}")

        return response


class DrillDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'drills/drills-delete.html'
    form_class = DrillDeleteForm
    model = Drill
    success_url = reverse_lazy('drill-dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.author != self.request.user:
            if not self.request.user.is_superuser:
                raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = self.get_object()

        if self.object.graphics:
            try:
                public_id = self.object.graphics.public_id
                destroy(public_id)
            except Exception as e:
                # Log the error (optional)
                print(f"Error deleting image from Cloudinary: {e}")

        return super().form_valid(form)

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
