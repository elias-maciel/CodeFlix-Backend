import uuid
from unittest.mock import create_autospec

import pytest

from core.category.domain.category_repository import (
    CategoryRepository,
)
from src.core.category.application.use_cases.delete_category import (
    DeleteCategory,
    DeleteCategoryRequest,
)
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.domain.category import Category


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
        category = Category(
            name="Movie",
            description="Description",
            is_active=True,
        )
        mock_repository = create_autospec(spec=CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = DeleteCategory(repository=mock_repository)
        request = DeleteCategoryRequest(id=category.id)
        use_case.execute(request=request)

        mock_repository.delete.assert_called_once_with(category.id)

    def test_when_category_not_found_then_raise_exception(self):
        mock_repository = create_autospec(spec=CategoryRepository)
        mock_repository.get_by_id.return_value = None

        use_case = DeleteCategory(repository=mock_repository)
        request = DeleteCategoryRequest(id=uuid.uuid4())
        with pytest.raises(CategoryNotFound):
            use_case.execute(request=request)

        mock_repository.delete.assert_not_called()
