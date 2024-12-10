from Domain.Database.BaseConnection import BaseConnection


class ImageRepository(BaseConnection):
    def __init__(self):
        BaseConnection.__init__(self)

        self.image_collection = self.database['image']

    def insert(self, data):
        result = self.image_collection.insert_one(data)
        return result.inserted_id

    def find_all(self):
        images = list(self.image_collection.find({}, {"_id": 1, "title": 1, "artist": 1, "category": 1}))
        for image in images:
            image["_id"] = str(image["_id"])
        return images

    def update(self, image_id, updated_data):
        result = self.image_collection.update_one({"_id": image_id}, {"$set": updated_data})
        return result.modified_count

    def delete(self, image_id):
        result = self.image_collection.delete_one({"_id": image_id})
        return result.deleted_count
