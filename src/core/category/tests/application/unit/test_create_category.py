from unittest.mock import MagicMock
from uuid import UUID

import pytest

from core.category.domain.category_repository import (
    CategoryRepository,
)
from src.core.category.application.use_cases.create_category import (
    CreateCategory,
    CreateCategoryRequest,
)
from src.core.category.application.use_cases.exceptions import (
    InvalidCategoryData,
)


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(spec=CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        create_category_request = CreateCategoryRequest(
            name="Movie",
            description="Description",
            is_active=True,
        )
        category_id = use_case.execute(request=create_category_request).id

        assert category_id is not None
        assert isinstance(category_id, UUID)
        assert mock_repository.save.called

    def test_create_category_with_invalid_data(self):
        with pytest.raises(InvalidCategoryData, match="name cannot be empty"):
            mock_repository = MagicMock(spec=CategoryRepository)
            use_case = CreateCategory(repository=mock_repository)
            create_category_request = CreateCategoryRequest(
                name="",
                description="Description",
                is_active=True,
            )
            use_case.execute(request=create_category_request)
