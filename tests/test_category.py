import unittest
from uuid import UUID

from code_flix.category import Category


class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with self.assertRaisesRegex(ValueError, "The name must have less than 255 characters"):
            Category("a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Movie")
        self.assertEqual(type(category.id), UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Movie")
        self.assertEqual(category.name, "Movie")
        self.assertEqual(category.description, "")
        self.assertTrue(category.is_active)

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Movie")
        self.assertTrue(category.is_active)


    def test_category_is_created_with_provided_values(self):
        category = Category(name="Movie", description="Description", is_active=False)
        self.assertEqual(category.name, "Movie")
        self.assertEqual(category.description, "Description")
        self.assertFalse(category.is_active)


    def test_category_as_string(self):
        category = Category(name="Movie", description="Description", is_active=False)
        self.assertEqual(str(category), "Movie - Description (False)")

    def test_category_as_repr(self):
        category = Category(name="Movie", description="Description", is_active=False)
        self.assertEqual(repr(category), "<Category Movie ({})>".format(category.id))


if __name__ == '__main__':
    unittest.main()
