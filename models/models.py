class City:
    def __init__(self, city_id, name, postal_code, longitude, latitude, country):
        self.id = city_id
        self.name = name
        self.postal_code = postal_code
        self.longitude = longitude
        self.latitude = latitude
        self.country = country

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "postal_code": self.postal_code,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "country": self.country
        }
