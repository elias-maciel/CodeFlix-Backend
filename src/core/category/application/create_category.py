from uuid import UUID

from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


def create_category(
    repository: InMemoryCategoryRepository,
    name: str,
    description: str = "",
    is_active: bool = True,
) -> UUID:
    try:
        category = Category(name=name, description=description, is_active=is_active)
    except ValueError as e:
        raise InvalidCategoryData(e)
    repository.save(category)
    return category.id
