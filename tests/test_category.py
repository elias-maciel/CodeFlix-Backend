import uuid
from uuid import UUID

import pytest

from code_flix.category import Category


class TestCategory():
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="The name must have less than 255 characters"):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Movie")
        assert isinstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Movie")
        assert category.name == "Movie"
        assert category.description == ""
        assert category.is_active

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Movie")
        assert category.is_active


    def test_category_is_created_with_provided_values(self):
        category = Category(name="Movie", description="Description", is_active=False)
        assert category.name == "Movie"
        assert category.description == "Description"
        assert not category.is_active


    def test_category_as_string(self):
        category = Category(name="Movie", description="Description", is_active=False)
        assert str(category) == "Movie - Description (False)"

    def test_category_as_repr(self):
        id = uuid.uuid4()
        category = Category(name="Movie", description="Description", is_active=False, id=id)
        assert repr(category) == f"<Category Movie ({id})>"
