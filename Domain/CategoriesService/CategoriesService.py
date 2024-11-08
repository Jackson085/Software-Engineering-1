from Domain.Database.DatabaseService import DatabaseService

class CategoriesService:
    def __init__(self):
        self.database_service = DatabaseService()


    def save_category(self, category):
        if isinstance(category, list):
            return self.database_service.save_categories(category)

        return self.database_service.save_categories([category])

    def get_categories(self):
        return self.database_service.get_categories()