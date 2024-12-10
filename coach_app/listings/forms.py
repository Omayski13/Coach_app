from django import forms

from coach_app.common.mixins import DisableFieldsMixin, AddAsterixToRequired
from coach_app.listings.mixins import ListingTextsMixin
from coach_app.listings.models import Listing


class ListingBaseForm(AddAsterixToRequired,ListingTextsMixin,forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ('author',)


class ListingCreateForm(ListingBaseForm):
    class Meta(ListingBaseForm.Meta):
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['club'].required = True
        self.fields['club'].error_messages = {
            'required': 'Полето "Отбор" е задължително.'
        }


class ListingDashboardForm(ListingBaseForm):
    pass


class ListingDetailForm(ListingBaseForm):
    pass


class ListingEditForm(ListingBaseForm):
    pass


class ListingDeleteForm(DisableFieldsMixin,ListingBaseForm):
    pass
