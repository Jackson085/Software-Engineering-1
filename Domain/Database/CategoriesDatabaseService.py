from typing import List

from Domain.Database.BaseConnection import BaseConnection


class CategoriesDatabaseService(BaseConnection):
    def __init__(self):
        BaseConnection.__init__(self)

        self.categories_collection = self.database['categories']

        if not self.categories_collection.find_one({"_id": "categories_list"}):
            self.categories_collection.insert_one({"_id": "categories_list", "categories": []})

    # region categories
    def save_category(self, category: str) -> None:
        self.categories_collection.update_one(
            {"_id": "categories_list"},
            {"$addToSet": {"categories": category}}
        )

    def get_categories(self) -> List[str]:
        document = self.categories_collection.find_one({"_id": "categories_list"})
        return document.get("categories", []) if document else []

    def delete_category(self, category: str) -> None:
        self.categories_collection.update_one(
            {"_id": "categories_list"},
            {"$pull": {"categories": category}}
        )
    # endregion
