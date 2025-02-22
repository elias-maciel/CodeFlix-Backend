from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase


# Create your tests here.
class TestCategoryAPI(APITestCase):
    def test_list_categories(self):
        url = "/api/categories/"
        response = self.client.get(url)

        expected_data = [
            {
                "id": "c71d6b9f-a549-4e43-b8cd-da6d430a47da",
                "name": "Movie",
                "description": "Movie description",
                "is_active": True,
            },
            {
                "id": "7dd821d6-094b-4144-a7bf-e42413fcc517",
                "name": "Documentary",
                "description": "Documentary description",
                "is_active": True,
            },
        ]
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
