from uuid import UUID

from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        repository = InMemoryCategoryRepository()
        use_case = CreateCategory(repository=repository)
        create_category_request = CreateCategoryRequest(
            name="Movie",
            description="Description",
            is_active=True,
        )
        category_id = use_case.execute(request=create_category_request).id

        saved_category = repository.categories[0]
        assert category_id is not None
        assert isinstance(category_id, UUID)
        assert len(repository.categories) == 1
        assert saved_category.name == "Movie"
        assert saved_category.description == "Description"
        assert saved_category.id == category_id