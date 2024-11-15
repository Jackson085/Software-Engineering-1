from flask import Blueprint, request, jsonify
from Domain.CategoriesService.CategoriesService import CategoriesService

categories_bp = Blueprint('categories', __name__)
categories_service = CategoriesService()

@categories_bp.route('/categories', methods=['GET'])
def get_categories():
    """
    Get all categories
    ---
    tags:
      - Categories
    summary: Retrieve all categories
    description: Fetches a list of all categories stored in the database.
    responses:
      200:
        description: A list of all categories
        content:
          application/json:
            schema:
              type: object
              properties:
                categories:
                  type: array
                  items:
                    type: string
              example:
                categories:
                  - "Technology"
                  - "Technology1"
      500:
        description: Internal Server Error
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
              example:
                message: "An error occurred while fetching categories"
    """
    try:
        categories = categories_service.get_categories()
        return jsonify({"categories": categories}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@categories_bp.route('/categories', methods=['POST'])
def add_category():
    """
    Add a new category
    ---
    tags:
      - Categories
    summary: Add a new category to the database.
    description: Adds a category if it doesn't already exist. Expects a JSON body with a single "category" field.
    parameters:
      - name: category
        in: body
        required: true
        schema:
          type: object
          properties:
            category:
              type: string
              description: The category name to be added.
              example: "Technology"
    responses:
      201:
        description: Category added successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Category added successfully"
      400:
        description: Invalid category or wrong format
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Invalid category or wrong format"
      409:
        description: Category already exists
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Category already exists"
      500:
        description: Internal server error
        schema:
          type: object
          properties:
            message:
              type: string
              example: "An error occurred"
    """
    data = request.get_json()
    category = data.get('category')

    try:
        categories_service.save_category(category)
        return jsonify({"message": "Category added successfully"}), 201

    except TypeError:
        return jsonify({"message": "Invalid category or wrong format"}), 400

    except KeyError:
        return jsonify({"message": "Category already exists"}), 409

    except Exception as e:
        return jsonify({"message": str(e)}), 500

@categories_bp.route('/categories', methods=['DELETE'])
def delete_category():
    """
    Delete an existing category
    ---
    tags:
      - Categories
    summary: Delete an existing category from the database.
    description: Deletes a specified category if it exists in the database. Expects a JSON body with a "category" field.
    parameters:
      - name: category
        in: body
        required: true
        schema:
          type: object
          properties:
            category:
              type: string
              description: The category name to be deleted.
              example: "Technology"
    responses:
      200:
        description: Category deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Category Technology deleted successfully"
      400:
        description: Invalid category or wrong format
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Invalid category or wrong format"
      404:
        description: Category does not exist
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Category does not exist"
      500:
        description: Internal server error
        schema:
          type: object
          properties:
            message:
              type: string
              example: "An error occurred"
    """
    data = request.get_json()
    category = data.get('category')

    try:
        categories_service.delete_category(category)
        return jsonify({"message": f"Category {category} deleted successfully"}), 200

    except TypeError:
        return jsonify({"message": "Invalid category or wrong format"}), 400

    except KeyError:
        return jsonify({"message": "Category does not exists"}), 404

    except Exception as e:
        return jsonify({"message": str(e)}), 500
