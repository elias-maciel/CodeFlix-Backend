import uuid
from dataclasses import dataclass, field


@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        self.validate()

    def __str__(self):
        return f"{self.name} - {self.description} ({self.is_active})"

    def __repr__(self):
        return f"<Category {self.name} ({self.id})>"

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.id == other.id

    def validate(self):
        if not self.name:
            raise ValueError("The name cannot be empty")
        if len(self.name) > 255:
            raise ValueError("The name must have less than 256 characters")


    def update(self, name: str, description: str= ""):
        self.name = name
        self.description = description

        self.validate()

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

