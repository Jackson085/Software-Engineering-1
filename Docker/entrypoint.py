from flask import Flask
from flasgger import Swagger
from flask_cors import CORS

from Remote.Categories.CategoriesController import categories_bp
from Remote.Validation.LoginController import login_app_bp
from Remote.Validation.RegisterController import register_app_bp

app = Flask(__name__)
CORS(app)

swagger = Swagger(app)

# Register Blueprints here ↓
app.register_blueprint(login_app_bp)
app.register_blueprint(register_app_bp)
app.register_blueprint(categories_bp)

if __name__ == '__main__':
    app.run(debug=True)