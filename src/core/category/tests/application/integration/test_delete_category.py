from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
        category = Category(
            name="Movie",
            description="Description",
            is_active=True,
        )
        repository = InMemoryCategoryRepository(categories=[category])

        use_case = DeleteCategory(repository=repository)
        request = DeleteCategoryRequest(id=category.id)

        assert repository.get_by_id(category.id) is not None
        use_case.execute(request=request)
        assert repository.get_by_id(category.id) is None
