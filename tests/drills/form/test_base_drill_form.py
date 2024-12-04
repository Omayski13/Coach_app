from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from coach_app.drills.forms import BaseDrillForm
from coach_app.drills.models import Drill





class TestBaseDrillForm(TestCase):

    UserModel = get_user_model()

    def setUp(self):
        self.valid_drill_data = {
            'for_age_group':'U5 - U6',
            'graphics':None,
            'name':'test_name',
            'objectives':'test_',
            'description':'test_description',
            'focus':'Подаване',
            'dimensions':'test_dimensions',
            'series':'test_series',
            'duration':5,
            'coaching_points':'test_coaching_points',
            'progression':'test_progression',
        }

    def test__form_is_valid__expect_true(self):
        form = BaseDrillForm(data=self.valid_drill_data)
        self.assertTrue(form.is_valid())

    def test__empty_for_age_group__expect_error(self):
        self.valid_drill_data['for_age_group'] = ''
        form = BaseDrillForm(data=self.valid_drill_data)
        self.assertFalse(form.is_valid())
        self.assertIn('for_age_group', form.errors)

    def test__empty_objectives__expect_error(self):
        self.valid_drill_data['objectives'] = ''
        form = BaseDrillForm(data=self.valid_drill_data)
        self.assertFalse(form.is_valid())
        self.assertIn('objectives', form.errors)

    def test__empty_focus__expect_error(self):
        self.valid_drill_data['focus'] = ''
        form = BaseDrillForm(data=self.valid_drill_data)
        self.assertFalse(form.is_valid())
        self.assertIn('focus', form.errors)

    def test__empty_dimensions__expect_error(self):
        self.valid_drill_data['dimensions'] = ''
        form = BaseDrillForm(data=self.valid_drill_data)
        self.assertFalse(form.is_valid())
        self.assertIn('dimensions', form.errors)

    def test__empty_series__expect_error(self):
        self.valid_drill_data['series'] = ''
        form = BaseDrillForm(data=self.valid_drill_data)
        self.assertFalse(form.is_valid())
        self.assertIn('series', form.errors)

    def test__empty_description__expect_error(self):
        self.valid_drill_data['description'] = ''
        form = BaseDrillForm(data=self.valid_drill_data)
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)

    def test__empty_coaching_points__expect_error(self):
        self.valid_drill_data['coaching_points'] = ''
        form = BaseDrillForm(data=self.valid_drill_data)
        self.assertFalse(form.is_valid())
        self.assertIn('coaching_points', form.errors)