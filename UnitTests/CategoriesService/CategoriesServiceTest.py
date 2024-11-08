import unittest
from unittest.mock import MagicMock, patch

from Domain.CategoriesService.CategoriesService import CategoriesService
from Domain.Database.DatabaseService import DatabaseService


class CategoriesServiceTest(unittest.TestCase):
    def setUp(self):
        patcher = patch(f"{CategoriesService.__module__}.{DatabaseService.__name__}")
        self.MockDatabaseService = patcher.start()
        self.addCleanup(patcher.stop)

        self.categories_service = CategoriesService()

        self.mock_db_service_instance = self.MockDatabaseService.return_value

    def test_save_category_single(self):
        category = "dsadasd"
        self.mock_db_service_instance.save_categories.return_value = None

        self.categories_service.save_category(category)

        self.mock_db_service_instance.save_categories.assert_called_once_with(["dsadasd"])

    # @patch(f"{CategoriesService.__module__}.{DatabaseService.__name__}")
    def test_save_category_multiple(self):
        categories = ["Sports", "Health"]

        self.mock_db_service_instance.save_categories.return_value = None

        self.categories_service.save_category(categories)

        self.mock_db_service_instance.save_categories.assert_called_once_with(["Sports", "Health"])

    def test_get_categories(self):
        mock_categories = ["Sports", "Technology", "Health"]
        self.mock_db_service_instance.get_categories.return_value = mock_categories

        result = self.categories_service.get_categories()

        self.mock_db_service_instance.get_categories.assert_called_once()

        self.assertEqual(result, mock_categories)


if __name__ == '__main__':
    unittest.main()