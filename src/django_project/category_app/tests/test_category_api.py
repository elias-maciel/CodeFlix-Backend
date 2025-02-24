import pytest
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APIClient

from core.category.domain.category import Category
from django_project.category_app.repository import DjangoORMCategoryRepository


@pytest.fixture
def category_movie():
    return Category(
        name="Movie",
        description="Movie description",
    )


@pytest.fixture
def category_documentary():
    return Category(
        name="Documentary",
        description="Documentary description",
    )


@pytest.fixture
def repository():
    return DjangoORMCategoryRepository()


@pytest.mark.django_db
class TestCategoryAPI:
    def test_list_categories(
        self,
        category_movie: Category,
        category_documentary: Category,
        repository: DjangoORMCategoryRepository,
    ):
        repository.save(category_movie)
        repository.save(category_documentary)
        url = "/api/categories/"
        response = APIClient().get(url)
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
        assert response.status_code == HTTP_200_OK
        assert len(response.data) == 2
        assert response.data == expected_data

@pytest.mark.django_db
class TestRetrieveAPI:
    def test_return_400_when_category_id_is_invalid(self):
        url = "/api/categories/invalid_id/"
        response = APIClient().get(url)
        assert response.status_code == HTTP_400_BAD_REQUEST

    def test_return_category_when_exists(
        self,
        category_movie: Category,
        category_documentary: Category,
        repository: DjangoORMCategoryRepository,
    ):
        repository.save(category_movie)
        repository.save(category_documentary)
        url = f"/api/categories/{category_documentary.id}/"
        response = APIClient().get(url)
        expected_data = {
            "id": str(category_documentary.id),
            "name": category_documentary.name,
            "description": category_documentary.description,
            "is_active": category_documentary.is_active,
        }
        assert response.status_code == HTTP_200_OK
        assert response.data == expected_data

    def test_return_404_when_category_not_exists(self):
        pass
