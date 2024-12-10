from django.db.models import Count


class DrillGraphicsTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['graphics'].label = 'Графика '
        self.fields['graphics'].widget.attrs.update({
            'class': 'wide-input-drills'
        })


class DrillNameTextMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Име * '
        self.fields['name'].widget.attrs.update({
            'placeholder': 'пример: 1 срещу 1 на тъча',
            'class': 'wide-input-drills'
        })
        self.fields['name'].error_messages = {
            'required': 'Полето "Име" е задължително.'
        }


class OrderFieldsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_order = []
        ordered_fields = {field: self.fields[field] for field in field_order if field in self.fields}
        self.fields = ordered_fields


class DrillTextsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        field_order = ['graphics', 'name', 'for_age_group', 'focus', 'objectives', 'dimensions', 'series', 'duration'
            , 'description', 'coaching_points', 'progression']
        ordered_fields = {field: self.fields[field] for field in field_order if field in self.fields}
        self.fields = ordered_fields

        self.fields['for_age_group'].required = True
        self.fields['for_age_group'].label = 'За възрастова група'
        self.fields['for_age_group'].widget.attrs.update({
            'class': 'wide-input-drills'
        })
        self.fields['for_age_group'].error_messages = {
            'required': 'Полето "За възрастова група" е задължително.'
        }

        self.fields['objectives'].required = True
        self.fields['objectives'].label = 'Цели'
        self.fields['objectives'].widget.attrs.update({
            'placeholder': 'пример: преодоляване на противник',
            'class': 'wide-input-drills'
        })
        self.fields['objectives'].error_messages = {
            'required': 'Полето "Цели" е задължително.'
        }

        self.fields['focus'].required = True
        self.fields['focus'].label = 'Фокус'
        self.fields['focus'].widget.attrs.update({
            'class': 'wide-input-drills'
        })
        self.fields['focus'].error_messages = {
            'required': 'Полето "Фокус" е задължително.'
        }

        self.fields['dimensions'].required = True
        self.fields['dimensions'].label = 'Размери'
        self.fields['dimensions'].widget.attrs.update({
            'placeholder': "пример: 20х20",
            'class': 'wide-input-drills'
        })
        self.fields['dimensions'].error_messages = {
            'required': 'Полето "Размери" е задължително.'
        }

        self.fields['series'].required = True
        self.fields['series'].label = 'Серии'
        self.fields['series'].widget.attrs.update({
            'placeholder': "пример: 2х3''",
            'class': 'wide-input-drills'
        })
        self.fields['series'].error_messages = {
            'required': 'Полето "Серии" е задължително.'
        }

        self.fields['duration'].label = 'Общо времетраене'
        self.fields['duration'].widget.attrs.update({
            'placeholder': "пример: 10",
            'class': 'wide-input-drills'
        })

        self.fields['description'].required = True
        self.fields['description'].label = 'Описание'
        self.fields['description'].widget.attrs.update({
            'placeholder': "Въведи описание на упражнението",
            'class': 'wide-input-drills'
        })
        self.fields['description'].error_messages = {
            'required': 'Полето "Описание" е задължително.'
        }

        self.fields['coaching_points'].required = True
        self.fields['coaching_points'].label = 'Треньорски цели'
        self.fields['coaching_points'].widget.attrs.update({
            'placeholder': "пример: правилно изпълнение на финтови движения",
            'class': 'wide-input-drills'
        })
        self.fields['coaching_points'].error_messages = {
            'required': 'Полето "Треньорски цели" е задължително.'
        }

        self.fields['progression'].label = 'Прогресия'
        self.fields['progression'].widget.attrs.update({
            'placeholder': "пример: добавяне на максимално време, в което защитникът да бъде преодолян",
            'class': 'wide-input-drills'
        })


class DrillFiltersMixin():
    def get_filtered_queryset(self, queryset):
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
