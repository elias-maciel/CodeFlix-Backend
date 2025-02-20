import uuid
from uuid import UUID

import pytest

from code_flix.category import Category


class TestCategory():
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="The name must have less than 256 characters"):
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

    def  test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="The name cannot be empty"):
            Category(name="")

class TestUpdateCategory():
    def test_update_category_with_name_and_description(self):
        category = Category(name="Movie", description="Description", is_active=False)
        category.update(name="New Movie", description="New Description")
        assert category.name == "New Movie"
        assert category.description == "New Description"

    def test_update_category_with_invalid_name(self):
        category = Category(name="Movie", description="Description", is_active=False)
        with pytest.raises(ValueError, match="The name must have less than 256 characters"):
            category.update(name="a" * 256, description="New Description")

    def test_update_category_with_empty_name(self):
        category = Category(name="Movie", description="Description", is_active=False)
        with pytest.raises(ValueError, match="The name cannot be empty"):
            category.update(name="", description="New Description")

class TestActivateCategory():
    def test_activate_category(self):
        category = Category(name="Movie", description="Description", is_active=False)
        category.activate()
        assert category.is_active

    def test_activate_category_is_active(self):
        category = Category(name="Movie", description="Description", is_active=True)
        category.activate()
        assert category.is_active

class TestDeactivateCategory():
    def test_deactivate_category(self):
        category = Category(name="Movie", description="Description", is_active=True)
        category.deactivate()
        assert not category.is_active

    def test_deactivate_category_is_inactive(self):
        category = Category(name="Movie", description="Description", is_active=False)
        category.deactivate()
        assert not category.is_active
