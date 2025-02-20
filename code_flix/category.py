import uuid


class Category:
    def __init__(self,
                 name,
                 id = "",
                 description= "",
                 is_active = True):
        self.id = id or uuid.uuid4()
        self.name = name
        self.description = description
        self.is_active = is_active

        self.validate()

    def validate(self):
        if len(self.name) > 255:
            raise ValueError("The name must have less than 256 characters")

    def __str__(self):
        return f"{self.name} - {self.description} ({self.is_active})"

    def __repr__(self):
        return f"<Category {self.name} ({self.id})>"

    def update_category(self, name: str, description: str=""):
        self.name = name
        self.description = description

        self.validate()

