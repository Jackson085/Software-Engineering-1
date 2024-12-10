from flask import Blueprint, request, jsonify
from Domain.ImageService.ImageService import ImageService
from Domain.Validation.TokenValidationService import admin_token_required

image_bp = Blueprint('image', __name__)
image_service = ImageService()

@image_bp.route('/images', methods=['POST'])
# @admin_token_required
def create_image():
    """
        Create Image
        ---
        tags:
          - Images
        summary: Create a new image
        description: Create a new image by providing all the necessary details such as category, title, artist, and dimensions. Returns the ID of the created image if successful, or an error message otherwise.
        parameters:
          - name: image_data
            in: body
            required: true
            schema:
              type: object
              required:
                - category
                - title
                - artist
                - motive_height
                - motive_width
                - sheet_height
                - sheet_width
                - price
                - photo_url
              properties:
                category:
                  type: string
                  example: "Originale"
                  description: "The category of the image (e.g., Originale, Reproduktionen, Grafiken)."
                title:
                  type: string
                  example: "Starry Night"
                  description: "The title of the image."
                artist:
                  type: string
                  example: "Vincent van Gogh"
                  description: "The artist who created the image."
                motive_height:
                  type: number
                  format: float
                  example: 50.0
                  description: "Height of the image motive in cm."
                motive_width:
                  type: number
                  format: float
                  example: 40.0
                  description: "Width of the image motive in cm."
                sheet_height:
                  type: number
                  format: float
                  example: 60.0
                  description: "Height of the image sheet in cm."
                sheet_width:
                  type: number
                  format: float
                  example: 50.0
                  description: "Width of the image sheet in cm."
                price:
                  type: number
                  format: float
                  example: 1500.00
                  description: "Price of the image in the chosen currency."
                photo_url:
                  type: string
                  format: uri
                  example: "https://example.com/images/starry-night.jpg"
                  description: "URL to the image's photo."
        responses:
          201:
            description: Image created successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Image created"
                image_id:
                  type: string
                  example: "64aef5d84f1e0e1234567890"
          400:
            description: Error occurred while creating the image
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Invalid or missing data"
        """
    data = request.get_json()
    try:
        image_id = image_service.create_image(data)
        return jsonify({"message": "Image created", "image_id": str(image_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@image_bp.route('/images', methods=['GET'])
def get_images():
    """
    Get All Images
    ---
    tags:
      - Images
    summary: Retrieve all images
    description: Fetch all images from the database, returning key information like category, title, artist, dimensions, and price.
    responses:
      200:
        description: A list of images
        schema:
          type: array
          items:
            type: object
            properties:
              image_id:
                type: string
                example: "64aef5d84f1e0e1234567890"
                description: "The unique identifier for the image."
              category:
                type: string
                example: "Originale"
                description: "The category of the image (e.g., Originale, Reproduktionen, Grafiken)."
              title:
                type: string
                example: "Starry Night"
                description: "The title of the image."
              artist:
                type: string
                example: "Vincent van Gogh"
                description: "The artist who created the image."
              motive_height:
                type: number
                format: float
                example: 50.0
                description: "Height of the image motive in cm."
              motive_width:
                type: number
                format: float
                example: 40.0
                description: "Width of the image motive in cm."
              sheet_height:
                type: number
                format: float
                example: 60.0
                description: "Height of the image sheet in cm."
              sheet_width:
                type: number
                format: float
                example: 50.0
                description: "Width of the image sheet in cm."
              price:
                type: number
                format: float
                example: 1500.00
                description: "Price of the image in the chosen currency."
              photo_url:
                type: string
                format: uri
                example: "https://example.com/images/starry-night.jpg"
                description: "URL to the image's photo."
      400:
        description: Error occurred while retrieving images
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to retrieve images"
    """
    try:
        images = image_service.get_all_images()
        return jsonify(images), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@image_bp.route('/images/<image_id>', methods=['PUT'])
# @admin_token_required
def update_image(image_id):
    """
    Update Image
    ---
    tags:
      - Images
    summary: Update an existing image
    description: Updates an image's details such as category, title, artist, dimensions, and price based on the provided image ID.
    parameters:
      - name: image_id
        in: path
        required: true
        type: string
        description: The unique identifier of the image to be updated.
        example: "64aef5d84f1e0e1234567890"
      - name: user_data
        in: body
        required: true
        schema:
          type: object
          properties:
            category:
              type: string
              example: "Reproduktionen"
              description: "The updated category of the image (e.g., Originale, Reproduktionen, Grafiken)."
            title:
              type: string
              example: "The Persistence of Memory"
              description: "The updated title of the image."
            artist:
              type: string
              example: "Salvador Dalí"
              description: "The updated artist name."
            motive_height:
              type: number
              format: float
              example: 30.0
              description: "Updated height of the image motive in cm."
            motive_width:
              type: number
              format: float
              example: 40.0
              description: "Updated width of the image motive in cm."
            sheet_height:
              type: number
              format: float
              example: 50.0
              description: "Updated height of the image sheet in cm."
            sheet_width:
              type: number
              format: float
              example: 60.0
              description: "Updated width of the image sheet in cm."
            price:
              type: number
              format: float
              example: 2000.00
              description: "Updated price of the image in the chosen currency."
            photo_url:
              type: string
              format: uri
              example: "https://example.com/images/persistence-of-memory.jpg"
              description: "Updated URL to the image's photo."
    responses:
      200:
        description: Image updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Image updated"
      400:
        description: Invalid input or error occurred
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to update the image"
      404:
        description: Image not found
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Image not found"
      500:
        description: Server error
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Internal server error"
    """
    data = request.get_json()
    try:
        image_service.update_image(image_id, data)
        return jsonify({"message": "Image updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@image_bp.route('/images/<image_id>', methods=['DELETE'])
# @admin_token_required
def delete_image(image_id):
    """
    Update Image
    ---
    tags:
      - Images
    summary: Update an existing image
    description: Updates an image's details such as category, title, artist, dimensions, and price based on the provided image ID.
    parameters:
      - name: image_id
        in: path
        required: true
        type: string
        description: The unique identifier of the image to be updated.
        example: "64aef5d84f1e0e1234567890"
      - name: user_data
        in: body
        required: true
        schema:
          type: object
          properties:
            category:
              type: string
              example: "Reproduktionen"
              description: "The updated category of the image (e.g., Originale, Reproduktionen, Grafiken)."
            title:
              type: string
              example: "The Persistence of Memory"
              description: "The updated title of the image."
            artist:
              type: string
              example: "Salvador Dalí"
              description: "The updated artist name."
            motive_height:
              type: number
              format: float
              example: 30.0
              description: "Updated height of the image motive in cm."
            motive_width:
              type: number
              format: float
              example: 40.0
              description: "Updated width of the image motive in cm."
            sheet_height:
              type: number
              format: float
              example: 50.0
              description: "Updated height of the image sheet in cm."
            sheet_width:
              type: number
              format: float
              example: 60.0
              description: "Updated width of the image sheet in cm."
            price:
              type: number
              format: float
              example: 2000.00
              description: "Updated price of the image in the chosen currency."
            photo_url:
              type: string
              format: uri
              example: "https://example.com/images/persistence-of-memory.jpg"
              description: "Updated URL to the image's photo."
    responses:
      200:
        description: Image updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Image updated"
      400:
        description: Invalid input or error occurred
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to update the image"
      404:
        description: Image not found
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Image not found"
      500:
        description: Server error
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Internal server error"
    """
    try:
        image_service.delete_image(image_id)
        return jsonify({"message": "Image deleted"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 400
