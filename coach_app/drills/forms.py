from django import forms

from coach_app.common.mixins import DisableFieldsMixin, AddAsterixToRequired
from coach_app.drills.mixins import DrillTextsMixin, DrillNameTextMixin, DrillGraphicsTextsMixin, OrderFieldsMixin
from coach_app.drills.models import Drill


class BaseDrillForm(AddAsterixToRequired,DrillTextsMixin,forms.ModelForm):
    class Meta:
        model = Drill
        exclude = ('author','created_at','updated_at', 'approved')


class DrillCreateForm(DrillGraphicsTextsMixin,DrillNameTextMixin,BaseDrillForm):
    def save(self,commit=True):
        drill = super().save(commit=False)
        drill.name = drill.name.capitalize()

        if commit:
            drill.save()

        return drill


class DrillEditForm(DrillGraphicsTextsMixin,DrillNameTextMixin,BaseDrillForm):
    pass


class DrillDeleteForm(DisableFieldsMixin,BaseDrillForm,OrderFieldsMixin):
    field_order = ['for_age_group', 'focus', 'objectives','dimensions','series','duration','description',
                   'coaching_points','progression']
    class Meta:
        model = Drill
        exclude = ('author', 'created_at', 'updated_at', 'name', 'graphics')


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=50,
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'search-field',
                'placeholder': 'Търси тренировка по име....'
            }

        )
    )



