from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.use_cases.exceptions import CategoryNotFound


@dataclass
class DeleteCategoryRequest:
    id: UUID


class DeleteCategory:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, request: DeleteCategoryRequest) -> None:
        category = self.repository.get_by_id(request.id)
        if category is None:
            raise CategoryNotFound(f"Category with id {request.id} not found")
        self.repository.delete(category.id)
