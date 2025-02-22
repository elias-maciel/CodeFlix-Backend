from unittest.mock import create_autospec

from core.category.domain.category_repository import (
    CategoryRepository,
)
from src.core.category.application.use_cases.update_category import (
    UpdateCategory,
    UpdateCategoryRequest,
)
from src.core.category.domain.category import Category


class TestUpdateCategory:
    def test_update_category_name(self):
        category = Category(
            name="Movie",
            description="Description",
            is_active=True,
        )
        mock_repository = create_autospec(spec=CategoryRepository)
        mock_repository.get_by_id.return_value = category
        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(id=category.id, name="Series")
        use_case.execute(request=request)

        assert category.name == "Series"
        mock_repository.update.assert_called_once_with(category)

    def test_update_category_description(self):
        category = Category(
            name="Movie",
            description="Description",
            is_active=True,
        )
        mock_repository = create_autospec(spec=CategoryRepository)
        mock_repository.get_by_id.return_value = category
        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(id=category.id, description="New Description")
        use_case.execute(request=request)

        assert category.description == "New Description"
        mock_repository.update.assert_called_once_with(category)

    def test_can_deactivate_category(self):
        category = Category(
            name="Movie",
            description="Description",
            is_active=True,
        )
        mock_repository = create_autospec(spec=CategoryRepository)
        mock_repository.get_by_id.return_value = category
        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(id=category.id, is_active=False)
        use_case.execute(request=request)

        assert category.is_active is False
        mock_repository.update.assert_called_once_with(category)

    def test_can_activate_category(self):
        category = Category(
            name="Movie",
            description="Description",
            is_active=False,
        )
        mock_repository = create_autospec(spec=CategoryRepository)
        mock_repository.get_by_id.return_value = category
        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(id=category.id, is_active=True)
        use_case.execute(request=request)

        assert category.is_active is True
        mock_repository.update.assert_called_once_with(category)
