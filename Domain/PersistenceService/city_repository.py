class CityRepository:
    def __init__(self):
        self.cities = []
        self.city_id_counter = 1

    def get_city(self, city_id):
        return next((city for city in self.cities if city["id"] == city_id), None)

    def list_cities(self):
        return self.cities

    def create_city(self, data):
        city = {
            "id": self.city_id_counter,
            "name": data["name"],
            "postal_code": data["postal_code"],
            "longitude": data["longitude"],
            "latitude": data["latitude"],
            "country": data["country"]
        }
        self.cities.append(city)
        self.city_id_counter += 1
        return city

    def update_city(self, city_id, data):
        city = self.get_city(city_id)
        if not city:
            raise KeyError("City not found")

        city.update({
            "name": data["name"],
            "postal_code": data["postal_code"],
            "longitude": data["longitude"],
            "latitude": data["latitude"],
            "country": data["country"]
        })
        return city

    def delete_city(self, city_id):
        city = self.get_city(city_id)
        if not city:
            return False
        self.cities = [c for c in self.cities if c["id"] != city_id]
        return True
