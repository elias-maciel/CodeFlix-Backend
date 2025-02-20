from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


class TestSave:
    def test_can_save_category(self):
        repository = InMemoryCategoryRepository()
        category = Category(
            name="Movie",
            description="Description",
        )
        repository.save(category)

        assert len(repository.categories) == 1
        assert repository.categories[0] == category

class TestGetById:
    def test_can_get_category_by_id(self):
        category = Category(
            name="Movie",
            description="Description",
        )
        repository = InMemoryCategoryRepository(categories=[category])
        result = repository.get_by_id(category.id)

        assert result == category
