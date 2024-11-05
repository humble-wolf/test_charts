from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

class ChartDataAPITests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.chart_data_url = reverse('chart-data-api')

    def test_chart_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('chart-view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample D3 Chart")


    def test_authentication_required(self):
        response = self.client.get(self.chart_data_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_request(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test the authenticated request
        response = self.client.get(self.chart_data_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"values": [10, 15, 20, 25, 30]})
