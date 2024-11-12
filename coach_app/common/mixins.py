from django.db import models

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