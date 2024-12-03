from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from django.core.exceptions import PermissionDenied

from coach_app.common.models import Like
from coach_app.drills.models import Drill


class TestViews(TestCase):

    def setUp(self):
        # Create users
        self.user = get_user_model().objects.create_user(username='testuser', password='password')

        # Create a dummy Cloudinary URL for testing
        cloudinary_image_url = 'https://res.cloudinary.com/your-cloud-name/image/upload/v1733242187/drills/rxrlkdrd52o4xfk3xmvz.jpg'

        # Create a drill with a mock Cloudinary URL (simulate Cloudinary image URL)
        self.drill = Drill.objects.create(
            name="Test Drill",
            objectives="Test objectives",
            description="Test description",
            focus="Test focus",
            dimensions="10x10",
            series="Test series",
            duration=10,
            coaching_points="Test coaching points",
            progression="Test progression",
            author=self.user,
            approved=True,
            graphics=None  # Simulate the Cloudinary image URL
        )


    def test_likes_functionality_like(self):
        """
        Test the likes functionality, ensuring a like can be added to a drill.
        """
        self.client.login(username='testuser', password='password')  # Log in as regular user

        # Ensure no like exists for the drill initially
        self.assertEqual(Like.objects.filter(to_drill=self.drill, user=self.user).count(), 0)

        # Like the drill
        response = self.client.get(reverse('like', args=[self.drill.pk]))

        # Check the like was added and the redirect was correct
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertRedirects(response, f'{reverse("drill-dashboard")}#{self.drill.pk}')
        self.assertEqual(Like.objects.filter(to_drill=self.drill, user=self.user).count(), 1)

    def test_likes_functionality_unlike(self):
        """
        Test the likes functionality, ensuring a like can be removed from a drill.
        """
        # First, like the drill to ensure there's an existing like
        Like.objects.create(to_drill=self.drill, user=self.user)

        self.client.login(username='testuser', password='password')  # Log in as regular user

        # Ensure the like exists initially
        self.assertEqual(Like.objects.filter(to_drill=self.drill, user=self.user).count(), 1)

        # Unlike the drill
        response = self.client.get(reverse('like', args=[self.drill.pk]))

        # Check the like was removed and the redirect was correct
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertRedirects(response, f'{reverse("drill-dashboard")}#{self.drill.pk}')
        self.assertEqual(Like.objects.filter(to_drill=self.drill, user=self.user).count(), 0)