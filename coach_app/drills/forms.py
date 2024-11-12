from django import forms

from coach_app.drills.mixins import DrillTextsMixin
from coach_app.drills.models import Drill


class BaseDrillForm(DrillTextsMixin,forms.ModelForm):
    class Meta:
        model = Drill
        exclude = ('author','created_at','updated_at')


class DrillCreateFrom(BaseDrillForm):
    pass


class DrillEditFrom(BaseDrillForm):
    pass


class DrillDeleteFrom(BaseDrillForm):
    pass


