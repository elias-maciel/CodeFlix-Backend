from uuid import UUID

from core.category.domain.category import Category
from core.category.domain.category_repository import CategoryRepository
from django_project.category_app.models import Category as CategoryORM


class DjangoORMCategoryRepository(CategoryRepository):
    def __init__(self, model: CategoryORM | None = None) -> None:
        self.category_model = model or CategoryORM

    def save(self, category: Category) -> None:
        self.category_model.objects.create(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active,
        )

    def get_by_id(self, id: UUID) -> Category | None:
        try:
            category = self.category_model.objects.get(id=id)
            return Category(
                id=category.id,
                name=category.name,
                description=category.description,
                is_active=category.is_active,
            )
        except self.category_model.DoesNotExist:
            return None

    def delete(self, id: UUID) -> None:
        self.category_model.objects.get(id=id).delete()

    def update(self, category: Category) -> None:
        self.category_model.objects.filter(id=category.id).update(
            name=category.name,
            description=category.description,
            is_active=category.is_active,
        )

    def list(self) -> list[Category]:
        return [
            Category(
                id=category.id,
                name=category.name,
                description=category.description,
                is_active=category.is_active,
            )
            for category in self.category_model.objects.all()
        ]
