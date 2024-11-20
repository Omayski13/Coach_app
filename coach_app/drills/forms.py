from django import forms

from coach_app.common.mixins import DisableFieldsMixin, AddAsterixToRequired
from coach_app.drills.mixins import DrillTextsMixin, DrillNameTextMixin, DrillGraphicsTextsMixin, OrderFieldsMixin
from coach_app.drills.models import Drill


class BaseDrillForm(AddAsterixToRequired,DrillTextsMixin,forms.ModelForm):
    class Meta:
        model = Drill
        exclude = ('author','created_at','updated_at', 'approved')



class DrillCreateForm(DrillGraphicsTextsMixin,DrillNameTextMixin,BaseDrillForm):
    pass


class DrillEditForm(DrillGraphicsTextsMixin,DrillNameTextMixin,BaseDrillForm):
    pass


class DrillDeleteForm(DisableFieldsMixin,BaseDrillForm,OrderFieldsMixin):
    field_order = ['for_age_group', 'focus', 'objectives','dimensions','series','duration','description','coaching_points','progression']
    class Meta:
        model = Drill
        exclude = ('author','created_at','updated_at','name','graphics')



