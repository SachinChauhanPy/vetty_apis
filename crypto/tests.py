from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_api_key.models import APIKey


class CoinListViewTest(APITestCase):
    def setUp(self):
        """
        Create an API key for the DRF API.
        """
        # Generate a DRF API key
        self.api_key, self.key = APIKey.objects.create_key(name="Test Key")

        # Prepare the Authorization header with the API key
        self.headers = {"HTTP_AUTHORIZATION": f"Api-Key {self.key}"}
        print("Setup completed: API Key generated and added to headers.")

    def test_coin_list_with_api_key(self):
        """
        Test the coin list endpoint with a valid API key in the Authorization header.
        """
        url = reverse("crypto_api:coin-list")
        print(f"Testing Coin List API: {url}")

        response = self.client.get(url, **self.headers)
        print(
            f"Response status: {response.status_code}, Response data: {response.data}"
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, response.data)
        self.assertIn("results", response.data)
        self.assertIsInstance(response.data["results"], list)

    def test_coin_categories_with_api_key(self):
        """
        Test the coin categories endpoint with a valid API key in the Authorization header.
        """
        url = reverse("crypto_api:coin-categories")
        print(f"Testing Coin Categories API: {url}")

        response = self.client.get(url, **self.headers)
        print(
            f"Response status: {response.status_code}, Response data: {response.data}"
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, response.data)
        self.assertIn("results", response.data)
        self.assertIsInstance(response.data["results"], list)

    def test_specific_coin_with_api_key(self):
        """
        Test the specific coin endpoint with a valid coin ID.
        """
        coin_id = "bitcoin"
        url = reverse("crypto_api:specific-coin", kwargs={"coin_id": coin_id})
        print(f"Testing Specific Coin API with coin_id={coin_id}: {url}")

        response = self.client.get(url, **self.headers)
        print(
            f"Response status: {response.status_code}, Response data: {response.data}"
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, response.data)
        self.assertEqual(response.data.get("id"), coin_id)
        self.assertIn("symbol", response.data)
        self.assertIn("name", response.data)

    def test_specific_coin_not_found(self):
        """
        Test the specific coin endpoint with an invalid coin ID.
        """
        coin_id = "invalidcoin"
        url = reverse("crypto_api:specific-coin", kwargs={"coin_id": coin_id})
        print(
            f"Testing Specific Coin API with invalid coin_id={coin_id}: {url}")

        response = self.client.get(url, **self.headers)
        print(
            f"Response status: {response.status_code}, Response data: {response.data}"
        )

        self.assertEqual(response.status_code,
                         status.HTTP_404_NOT_FOUND, response.data)
        self.assertIn("error", response.data)

    def test_health_check_with_api_key(self):
        """
        Test the health check endpoint with a valid API key.
        """
        # Define the endpoint URL
        url = reverse("crypto_api:health-check")
        print(f"Testing Health Check API: {url}")

        # Make the GET request with the Authorization header
        response = self.client.get(url, **self.headers)
        print(
            f"Response status: {response.status_code}, Response data: {response.data}"
        )

        # Assertions
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, response.data)
        self.assertEqual(response.data.get("status"), "healthy")
        self.assertIn("message", response.data)
