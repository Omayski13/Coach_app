from PIL import Image
from cloudinary import CloudinaryResource
from cloudinary.uploader import destroy
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import models

from coach_app.choices import AgeGroupsChoices


class DisableFieldsMixin():
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'


class AddAsterixToRequired():
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            if field.required:
                field.label = f'{field.label} * '


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class UpdatedAtMixin(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True,
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
        abstract = True

class DeleteCloudinaryFormValidMixin():
    cloudinary_delete_field = None

    def form_valid(self, form):
        if not self.cloudinary_delete_field:
            raise ValueError("The 'cloudinary_delete_field' attribute must be set.")

        old_picture = getattr(self.get_object(), self.cloudinary_delete_field)
        response = super().form_valid(form)
        new_picture = getattr(self.object, self.cloudinary_delete_field)

        if old_picture and old_picture != new_picture:
            try:
                destroy(old_picture.public_id)
            except Exception as e:
                print(f"Error deleting old file from Cloudinary: {e}")

        return response



        old_profile_picture = self.cloudinary_delete_field()

        response = super().form_valid(form)

        new_profile_picture = self.object.profile_picture
        if old_profile_picture != new_profile_picture and old_profile_picture:
            try:
                public_id = old_profile_picture.public_id
                destroy(public_id)
            except Exception as e:
                print(f"Error deleting old graphics from Cloudinary: {e}")

        return response


class CloudinaryImageValidatorMixin():
    def validate_field(self, field_name):
        field_value = self.cleaned_data.get(field_name)

        if isinstance(field_value,CloudinaryResource):
            return field_value

        if field_value:
            try:
                img = Image.open(field_value)
                img.verify()  # Ensure the file is a valid image
                return field_value
            except Exception:
                raise ValidationError('Това поле трябва да бъде изображение.')

        return field_value

