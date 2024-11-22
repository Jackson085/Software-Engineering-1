from flask import Flask, request, jsonify, abort
from flasgger import Swagger
from Domain.CityService.city_service import CityService

app = Flask(__name__)
swagger = Swagger(app)
city_service = CityService()

@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    """
    Get a city by ID
    ---
    parameters:
      - name: city_id
        in: path
        type: integer
        required: true
        description: ID of the city to retrieve
    responses:
      200:
        description: A city object
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            postal_code:
              type: string
            longitude:
              type: number
            latitude:
              type: number
            country:
              type: string
      404:
        description: City not found
    """
    city = city_service.get_city(city_id)
    if not city:
        abort(404, description="City not found")
    return jsonify(city)

@app.route('/cities', methods=['GET'])
def list_cities():
    """
    List all cities
    ---
    responses:
      200:
        description: A list of cities
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              postal_code:
                type: string
              longitude:
                type: number
              latitude:
                type: number
              country:
                type: string
    """
    return jsonify(city_service.list_cities())

@app.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    """
    Update a city's attributes
    ---
    parameters:
      - name: city_id
        in: path
        type: integer
        required: true
        description: ID of the city to update
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            postal_code:
              type: string
            longitude:
              type: number
            latitude:
              type: number
            country:
              type: string
    responses:
      200:
        description: Updated city object
      400:
        description: Validation error
      404:
        description: City not found
    """
    data = request.json
    try:
        city = city_service.update_city(city_id, data)
        return jsonify(city)
    except ValueError as e:
        abort(400, description=str(e))
    except KeyError:
        abort(404, description="City not found")

@app.route('/cities', methods=['POST'])
def create_city():
    """
    Create a new city
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            postal_code:
              type: string
            longitude:
              type: number
            latitude:
              type: number
            country:
              type: string
    responses:
      201:
        description: City created
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            postal_code:
              type: string
            longitude:
              type: number
            latitude:
              type: number
            country:
              type: string
      400:
        description: Validation error
    """
    data = request.json
    try:
        city = city_service.create_city(data)
        return jsonify(city), 201
    except ValueError as e:
        abort(400, description=str(e))

@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    Delete a city by ID
    ---
    parameters:
      - name: city_id
        in: path
        type: integer
        required: true
        description: ID of the city to delete
    responses:
      204:
        description: City deleted successfully
      404:
        description: City not found
    """
    if city_service.delete_city(city_id):
        return '', 204
    abort(404, description="City not found")

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error.description)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error.description)}), 404

if __name__ == '__main__':
    app.run(debug=True)
