from bson.objectid import ObjectId

from Domain.Database.ImageRepository import ImageRepository


class ImageService:
    def __init__(self):
        self.image_repo = ImageRepository()

    def create_image(self, data):
        required_fields = ["category", "title", "artist", "motive_height", "motive_width",
                           "sheet_height", "sheet_width", "price", "photo_url"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing field: {field}")

        # Add default values
        data["status"] = "available"
        return self.image_repo.insert(data)

    def get_all_images(self):
        return self.image_repo.find_all()

    def update_image(self, image_id, data) -> None:
        if not ObjectId.is_valid(image_id):
            raise ValueError("Invalid image ID")

        updated_count = self.image_repo.update(ObjectId(image_id), data)
        if updated_count == 0:
            raise ValueError("Image not found")

    def delete_image(self, image_id) -> None:
        if not ObjectId.is_valid(image_id):
            raise ValueError("Invalid image ID")

        deleted_count = self.image_repo.delete(ObjectId(image_id))
        if deleted_count == 0:
            raise ValueError("Image not found")
