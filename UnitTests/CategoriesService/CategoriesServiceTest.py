import unittest
from unittest.mock import patch
from Domain.CategoriesService.CategoriesService import CategoriesService
from Domain.Database.CategoriesDatabaseService import CategoriesDatabaseService


class CategoriesServiceTest(unittest.TestCase):
    def setUp(self):
        patcher = patch(f"{CategoriesService.__module__}.{CategoriesDatabaseService.__name__}")
        self.MockCategoriesDatabaseService = patcher.start()
        self.addCleanup(patcher.stop)

        self.categories_service = CategoriesService()
        self.mock_db_service_instance = self.MockCategoriesDatabaseService.return_value

    def test_save_category_single_success(self):
        category = "Technology"
        self.mock_db_service_instance.get_categories.return_value = ["Health", "Sports"]

        self.categories_service.save_category(category)
        self.mock_db_service_instance.save_category.assert_called_once_with("Technology")

    def test_save_category_duplicate_error(self):
        category = "Health"
        self.mock_db_service_instance.get_categories.return_value = ["Health", "Sports"]

        with self.assertRaises(KeyError) as context:
            self.categories_service.save_category(category)
        self.assertEqual(str(context.exception), "'Health already exists'")

    def test_save_category_empty_error(self):
        category = ""
        with self.assertRaises(TypeError) as context:
            self.categories_service.save_category(category)
        self.assertEqual(str(context.exception), "category is None or empty")

    def test_get_categories(self):
        mock_categories = ["Sports", "Technology", "Health"]
        self.mock_db_service_instance.get_categories.return_value = mock_categories

        result = self.categories_service.get_categories()

        self.mock_db_service_instance.get_categories.assert_called_once()
        self.assertEqual(result, mock_categories)

    def test_delete_category_success(self):
        category = "Health"
        self.mock_db_service_instance.get_categories.return_value = ["Health", "Sports"]

        self.categories_service.delete_category(category)
        self.mock_db_service_instance.delete_category.assert_called_once_with("Health")

    def test_delete_category_not_found_error(self):
        category = "NonExistingCategory"
        self.mock_db_service_instance.get_categories.return_value = ["Health", "Sports"]

        with self.assertRaises(KeyError) as context:
            self.categories_service.delete_category(category)
        self.assertEqual(str(context.exception), "'NonExistingCategory does not exists'")

    def test_delete_category_empty_error(self):
        category = ""
        with self.assertRaises(TypeError) as context:
            self.categories_service.delete_category(category)
        self.assertEqual(str(context.exception), "category is None or empty")


if __name__ == '__main__':
    unittest.main()