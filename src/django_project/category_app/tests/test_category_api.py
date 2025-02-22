from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from core.category.domain.category import Category
from django_project.category_app.repository import DjangoORMCategoryRepository


# Create your tests here.
class TestCategoryAPI(APITestCase):
    def test_list_categories(self):
        category_movie = Category(
            name="Movie",
            description="Movie description",
        )
        category_documentary = Category(
            name="Documentary",
            description="Documentary description",
        )
        repository = DjangoORMCategoryRepository()
        repository.save(category_movie)
        repository.save(category_documentary)
        url = "/api/categories/"
        response = self.client.get(url)
        expected_data = [
            {
                "id": str(category_movie.id),
                "name": category_movie.name,
                "description": category_movie.description,
                "is_active": category_movie.is_active,
            },
            {
                "id": str(category_documentary.id),
                "name": category_documentary.name,
                "description": category_documentary.description,
                "is_active": category_documentary.is_active,
            },
        ]
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
