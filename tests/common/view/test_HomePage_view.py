from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()

class TestHomePageView(TestCase):

    def test__get_template_names__authentificated_user__returns_auth_template(self):
        user = UserModel.objects.create_user(
            username='testuser',
            email="testemail@admin.com",
            password='testpassword',
        )

        self.client.login(
            email="testemail@admin.com",
            password='testpassword'
        )
        response = self.client.get(reverse('home-page'))

        self.assertEqual(response.template_name, ['common/home-page-not-logged.html'])

    def test__get_template_names_with_anonymous_user__returns_not_logged_template(self):
        user = AnonymousUser

        response = self.client.get(reverse('home-page'))

        self.assertEqual(response.template_name, ['common/home-page-not-logged.html'])