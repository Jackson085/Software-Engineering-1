from Domain.PersistenceService.city_repository import CityRepository


class CityService:
    SUPPORTED_COUNTRIES = {"DE": "Germany", "FR": "France", "GB": "United Kingdom"}

    def __init__(self):
        self.repository = CityRepository()

    def validate_city_data(self, data):
        required_fields = {"name", "postal_code", "longitude", "latitude", "country"}

        if not all(field in data for field in required_fields):
            raise ValueError("Missing required fields")

        if data["country"] not in self.SUPPORTED_COUNTRIES:
            raise ValueError("Unsupported country")

        if data["country"] == "DE" and not data["postal_code"].isdigit():
            raise ValueError("Postal code for Germany must contain only digits")

    def get_city(self, city_id):
        return self.repository.get_city(city_id)

    def list_cities(self):
        return self.repository.list_cities()

    def create_city(self, data):
        self.validate_city_data(data)
        return self.repository.create_city(data)

    def update_city(self, city_id, data):
        self.validate_city_data(data)
        return self.repository.update_city(city_id, data)

    def delete_city(self, city_id):
        return self.repository.delete_city(city_id)
