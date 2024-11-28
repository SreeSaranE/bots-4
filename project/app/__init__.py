from flask import Flask, jsonify
from flask_cors import CORS
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    from .routes.webhook_routes import webhook_bp
    app.register_blueprint(webhook_bp, url_prefix='/api')
    
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"status": "active", "message": "Zoho SalesIQ Chatbot is running"}), 200
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Resource not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app