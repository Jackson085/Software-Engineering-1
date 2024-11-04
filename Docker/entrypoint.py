from flask import Flask
from flasgger import Swagger
from Remote.Validation.login import auth_bp

app = Flask(__name__)

swagger = Swagger(app)

# Register Blueprints here ↓
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)