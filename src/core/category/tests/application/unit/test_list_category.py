from unittest.mock import create_autospec

from core.category.domain.category_repository import (
    CategoryRepository,
)
from src.core.category.application.use_cases.list_category import (
    CategoryOutput,
    ListCategory,
    ListCategoryRequest,
    ListCategoryResponse,
)
from src.core.category.domain.category import Category


class TestListCategory:
    def test_when_no_categories_in_repository_then_return_empty_list(self):
        mock_repository = create_autospec(spec=CategoryRepository)
        mock_repository.list.return_value = []
        use_case = ListCategory(repository=mock_repository)
        request = ListCategoryRequest()

        response = use_case.execute(request=request)

        assert response == ListCategoryResponse(data=[])

    def test_when_categories_in_repository_then_return_list(self):
        category_movie = Category(
            name="Movie",
            description="Description",
            is_active=True,
        )
        category_series = Category(
            name="Series",
            description="Description",
            is_active=True,
        )
        mock_repository = create_autospec(spec=CategoryRepository)
        mock_repository.list.return_value = [category_movie, category_series]
        use_case = ListCategory(repository=mock_repository)
        request = ListCategoryRequest()

        response = use_case.execute(request=request)

        assert response == ListCategoryResponse(
            data=[
                CategoryOutput(
                    id=category_movie.id,
                    name=category_movie.name,
                    description=category_movie.description,
                    is_active=category_movie.is_active,
                ),
                CategoryOutput(
                    id=category_series.id,
                    name=category_series.name,
                    description=category_series.description,
                    is_active=category_series.is_active,
                ),
            ]
        )
