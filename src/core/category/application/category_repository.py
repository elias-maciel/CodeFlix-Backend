from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from src.core.category.domain.category import Category


class CategoryRepository(ABC):
    @abstractmethod
    def save(self, category: Category):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: UUID) -> Category | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: UUID):
        raise NotImplementedError

    @abstractmethod
    def update(self, category: Category):
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Category]:
        raise NotImplementedError
