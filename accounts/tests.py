from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class CreateAPIKeyTest(APITestCase):
    def setUp(self):
        """
        Set up a test user and authenticate them.
        """
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.client.login(username="testuser", password="password123")
        self.url = reverse("accounts_api:create_api_key")

    def test_create_api_key_success(self):
        """
        Test that the API key is successfully created and returned for an authenticated user.
        """
        response = self.client.post(self.url)
        if response.status_code == status.HTTP_201_CREATED:
            print("Test Passed: API key successfully created for authenticated user.")
        else:
            print("Test Failed: Unable to create API key.")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("api_key", response.data)
        self.assertIsNotNone(response.data["api_key"])

    def test_create_api_key_unauthenticated(self):
        """
        Test that an unauthenticated user cannot access the endpoint.
        """
        self.client.logout()
        response = self.client.post(self.url)
        if response.status_code == status.HTTP_403_FORBIDDEN:
            print(
                "Test Passed: Unauthenticated user is forbidden from creating API keys."
            )
        else:
            print("Test Failed: Unauthenticated user was allowed to create an API key.")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
