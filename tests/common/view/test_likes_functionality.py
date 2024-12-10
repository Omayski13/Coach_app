from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from django.core.exceptions import PermissionDenied

from coach_app.common.models import Like
from coach_app.drills.models import Drill


class TestViews(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')

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
        self.client.login(username='testuser', password='password')

        self.assertEqual(Like.objects.filter(to_drill=self.drill, user=self.user).count(), 0)

        response = self.client.get(reverse('like', args=[self.drill.pk]))

        self.assertRedirects(response, f'{reverse("drill-dashboard")}#{self.drill.pk}')
        self.assertEqual(Like.objects.filter(to_drill=self.drill, user=self.user).count(), 1)

    def test_likes_functionality_unlike(self):

        Like.objects.create(to_drill=self.drill, user=self.user)

        self.client.login(username='testuser', password='password')  # Log in as regular user

        self.assertEqual(Like.objects.filter(to_drill=self.drill, user=self.user).count(), 1)

        response = self.client.get(reverse('like', args=[self.drill.pk]))

        self.assertRedirects(response, f'{reverse("drill-dashboard")}#{self.drill.pk}')
        self.assertEqual(Like.objects.filter(to_drill=self.drill, user=self.user).count(), 0)