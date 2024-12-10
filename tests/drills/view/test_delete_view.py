from io import BytesIO


from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from coach_app.drills.models import Drill

UserModel = get_user_model()

class DrillDeleteViewTests(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='testemail@mail.com',
            password='password'
        )

        self.drill = Drill.objects.create(
            name='Test Drill',
            objectives='Test objectives',
            description='Test description',
            focus='Technical',
            dimensions='5x5',
            series='Series A',
            author=self.user,
            approved=True,
            graphics=None
        )

        self.client.login(username='testuser', password='password')


    def test_drill_delete_view_permission(self):
        another_user = UserModel.objects.create_user(
            username='anotheruser',
            email='anotheremail@mail.com',
            password='password'
        )
        self.client.login(username='anotheruser', password='password')

        url = reverse('drill-delete', args=[self.drill.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)


    def test_drill_delete_view_invalid_drill(self):
        url = reverse('drill-delete', args=[999])  # assuming 999 doesn't exist
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)