from flask import Flask
from backend.routes.api import api_bp
from backend.routes.auth import auth_bp
from backend.routes.shipment import shipment_bp
from backend.routes.dashboard import dashboard_bp

app = Flask(__name__)
app.secret_key = "super_secret_key"

# Registro de Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(shipment_bp)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)