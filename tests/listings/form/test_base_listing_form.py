from django.test import TestCase

from coach_app.listings.forms import ListingBaseForm


class TestBaseListingForm(TestCase):
    def setUp(self):
        self.valid_listing_data = {
            'for_age_group': 'U5 - U6',
            'club': 'test',
            'experience_needed': 2,
            'licence_required': 'Без лиценз',
            'salary': 1000,
            'telephone_number': '0888888888880',
            'contact_person': 'test person',
            'position': 'test position',
        }

    def test__form_is_valid__expect_true(self):
        form = ListingBaseForm(data=self.valid_listing_data)
        self.assertTrue(form.is_valid())

    def test__empty_club__expect_error(self):
        self.valid_listing_data['club'] = ''
        form = ListingBaseForm(data=self.valid_listing_data)
        self.assertFalse(form.is_valid())
        self.assertIn('club', form.errors)

    def test__empty_licence_required__expect_error(self):
        self.valid_listing_data['licence_required'] = ''
        form = ListingBaseForm(data=self.valid_listing_data)
        self.assertFalse(form.is_valid())
        self.assertIn('licence_required', form.errors)

    def test__telephone_number_with_9_numbers__expect_error(self):
        self.valid_listing_data['telephone_number'] = '123456789'
        form = ListingBaseForm(data=self.valid_listing_data)
        self.assertFalse(form.is_valid())
        self.assertIn('telephone_number', form.errors)

    def test__telephone_number_with_14_numbers__expect_error(self):
        self.valid_listing_data['telephone_number'] = '12345678911111'
        form = ListingBaseForm(data=self.valid_listing_data)
        self.assertFalse(form.is_valid())
        self.assertIn('telephone_number', form.errors)

    def test__empty_contact_person__expect_error(self):
        self.valid_listing_data['contact_person'] = ''
        form = ListingBaseForm(data=self.valid_listing_data)
        self.assertFalse(form.is_valid())
        self.assertIn('contact_person', form.errors)