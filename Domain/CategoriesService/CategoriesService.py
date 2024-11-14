from typing import List
from Domain.Database.CategoriesDatabaseService import CategoriesDatabaseService


class CategoriesService:
    def __init__(self):
        self.database_service = CategoriesDatabaseService()

    def get_categories(self) -> List[str]:
        return self.database_service.get_categories()

    def save_category(self, category: str):
        if category in self.get_categories():
            raise KeyError(f'{category} already exists')

        if not category:
            raise TypeError('category is None or empty')

        return self.database_service.save_category(category)

    def delete_category(self, category):
        if not category:
            raise TypeError('category is None or empty')

        if category not in self.get_categories():
            raise KeyError(f'{category} does not exists')

        self.database_service.delete_category(category)
