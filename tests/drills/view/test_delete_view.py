from io import BytesIO


from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from coach_app.drills.models import Drill

UserModel = get_user_model()

class DrillDeleteViewTests(TestCase):



    def setUp(self):

        # Create a test user
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='testemail@mail.com',
            password='password'
        )

        # Create a drill instance with a mock image
        self.drill = Drill.objects.create(
            name='Test Drill',
            objectives='Test objectives',
            description='Test description',
            focus='Technical',  # Assuming 'FocusChoices' contains 'Technical'
            dimensions='5x5',
            series='Series A',
            author=self.user,
            approved=True,
            graphics=None  # Attach the mock image
        )

        # Authenticate the user
        self.client.login(username='testuser', password='password')



    def test_drill_delete_view_permission(self):
        # Test if a user who is not the owner of the drill is prevented from deleting it
        another_user = UserModel.objects.create_user(
            username='anotheruser',
            email='anotheremail@mail.com',
            password='password'
        )
        self.client.login(username='anotheruser', password='password')

        url = reverse('drill-delete', args=[self.drill.pk])
        response = self.client.get(url)

        # The response should be a 403 Forbidden (user does not have permission)
        self.assertEqual(response.status_code, 403)


    def test_drill_delete_view_invalid_drill(self):
        # Test if a non-existent drill gives a 404 error
        url = reverse('drill-delete', args=[999])  # assuming 999 doesn't exist
        response = self.client.get(url)

        # Check for a 404 error when the drill does not exist
        self.assertEqual(response.status_code, 404)