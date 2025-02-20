from unittest.mock import MagicMock
from uuid import UUID

import pytest

from src.core.category.application.create_category import (
    create_category,
)
from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(spec=InMemoryCategoryRepository)
        category_id = create_category(
            repository=mock_repository,
            name="Movie",
            description="Description",
            is_active=True,
        )

        assert category_id is not None
        assert isinstance(category_id, UUID)
        assert mock_repository.save.called

    def test_create_category_with_invalid_data(self):
        with pytest.raises(InvalidCategoryData, match="name cannot be empty"):
            mock_repository = MagicMock(spec=InMemoryCategoryRepository)
            create_category(repository=mock_repository, name="")
