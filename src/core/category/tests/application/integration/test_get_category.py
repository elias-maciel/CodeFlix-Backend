import uuid

import pytest

from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.application.use_cases.get_category import (
    GetCategory,
    GetCategoryRequest,
    GetCategoryResponse,
)
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


class TestGetCategory:
    def test_get_category_by_id(self):
        category_movies = Category(
            name="Movie",
            description="Description",
        )
        category_series = Category(
            name="Series",
            description="Description",
        )
        repository = InMemoryCategoryRepository(
            categories=[category_movies, category_series]
        )
        use_case = GetCategory(repository=repository)
        request = GetCategoryRequest(id=category_movies.id)
        response = use_case.execute(request=request)

        assert response == GetCategoryResponse(
            id=category_movies.id,
            name="Movie",
            description="Description",
            is_active=True,
        )

    def test_when_category_does_not_exists_then_raise_exception(self):
        category_movies = Category(
            name="Movie",
            description="Description",
        )
        category_series = Category(
            name="Series",
            description="Description",
        )
        repository = InMemoryCategoryRepository(
            categories=[category_movies, category_series]
        )
        use_case = GetCategory(repository=repository)
        not_found_id = uuid.uuid4()
        request = GetCategoryRequest(id=not_found_id)
        with pytest.raises(CategoryNotFound) as exc:
            use_case.execute(request=request)
