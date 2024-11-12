from django.db import models

from coach_app.choices import AgeGroupsChoices


class DisableFieldsMixin():
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class UpdatedAtMixin(models.Model):
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class ForAgeGroupMixin(models.Model):
    for_age_group = models.CharField(
        max_length=30,
        choices=AgeGroupsChoices.choices,
        null=True,
        blank=True,
    )

    class Meta:
        abstract=True