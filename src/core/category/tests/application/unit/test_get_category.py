from unittest.mock import create_autospec

from core.category.domain.category_repository import (
    CategoryRepository,
)
from src.core.category.application.use_cases.get_category import (
    GetCategory,
    GetCategoryRequest,
    GetCategoryResponse,
)
from src.core.category.domain.category import Category


class TestGetCategory:
    def test_return_found_category(self):
        category = Category(
            name="Movie",
            description="Description",
            is_active=True,
        )
        mock_repository = create_autospec(spec=CategoryRepository)
        mock_repository.get_by_id.return_value = category
        use_case = GetCategory(repository=mock_repository)
        request = GetCategoryRequest(id=category.id)
        response = use_case.execute(request=request)

        assert response == GetCategoryResponse(
            id=category.id,
            name="Movie",
            description="Description",
            is_active=True,
        )
