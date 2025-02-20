from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import (
    CategoryRepository,
)
from src.core.category.application.use_cases.exceptions import (
    InvalidCategoryData,
)


@dataclass
class UpdateCategoryRequest:
    id: UUID
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None


class UpdateCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, request: UpdateCategoryRequest):
        category = self.repository.get_by_id(request.id)
        if category is None:
            raise Exception("Category not found")
        current_name = category.name
        current_description = category.description
        if request.name:
            current_name = request.name
        if request.description:
            current_description = request.description
        try:
            category.update(
                name=current_name,
                description=current_description,
            )
        except ValueError as e:
            raise InvalidCategoryData(e)

        if request.is_active is True:
            category.activate()
        if request.is_active is False:
            category.deactivate()

        self.repository.update(category)
        return category
