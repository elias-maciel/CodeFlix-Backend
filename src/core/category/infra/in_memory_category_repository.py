from uuid import UUID

from src.core.category.application.category_repository import (
    CategoryRepository,
)
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.domain.category import Category


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories=None):
        self.categories = categories or []

    def save(self, category: Category):
        self.categories.append(category)

    def get_by_id(self, id: UUID) -> Category | None:
        for category in self.categories:
            if category.id == id:
                return category
        return None

    def delete(self, id: UUID):
        self.categories = [
            category for category in self.categories if category.id != id
        ]

    def update(self, category: Category):
        old_category = self.get_by_id(category.id)
        if old_category:
            self.delete(category.id)
            self.save(category)
        else:
            raise CategoryNotFound("Category not found")

    def list(self) -> list[Category]:
        return [category for category in self.categories]
