from django import forms

from coach_app.common.mixins import DisableFieldsMixin
from coach_app.drills.mixins import DrillTextsMixin, DrillNameTextMixin, DrillGraphicsTextsMixin
from coach_app.drills.models import Drill


class BaseDrillForm(DrillTextsMixin,forms.ModelForm):
    class Meta:
        model = Drill
        exclude = ('author','created_at','updated_at')



class DrillCreateForm(DrillGraphicsTextsMixin,DrillNameTextMixin,BaseDrillForm):
    pass


class DrillEditForm(BaseDrillForm):
    pass


class DrillDeleteForm(DisableFieldsMixin,BaseDrillForm):
    field_order = ['for_age_group', 'focus', 'objectives','dimensions','series','duration','description','coaching_points','progression']
    class Meta:
        model = Drill
        exclude = ('author','created_at','updated_at','name','graphics')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_order = ['for_age_group', 'focus', 'objectives','dimensions','series','duration'
            ,'description','coaching_points','progression']
        ordered_fields = {field: self.fields[field] for field in field_order if field in self.fields}
        self.fields = ordered_fields

