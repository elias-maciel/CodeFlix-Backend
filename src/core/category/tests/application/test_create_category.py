from uuid import UUID

import pytest

from src.core.category.application.create_category import create_category, InvalidCategoryData


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        category_id = create_category(
            name="Movie", description="Description", is_active=True
        )

        assert category_id is not None
        assert isinstance(category_id, UUID)

    def test_create_category_with_invalid_data(self):
        with pytest.raises(InvalidCategoryData, match="name cannot be empty"):
             create_category(name="")

