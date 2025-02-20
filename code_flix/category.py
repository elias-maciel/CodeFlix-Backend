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

    def __str__(self):
        return f"{self.name} - {self.description} ({self.is_active})"

    def __repr__(self):
        return f"<Category {self.name} ({self.id})>"

    def __eq__(self, other):
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

