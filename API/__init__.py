from flask import Flask,jsonify
from flask_restx import Api
from .config.config import config_dict
from .utils import db
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from .views import weatherNameSpace




# creating the flask application
def create_app(config=config_dict["dev"]):
    app=Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    migrate=Migrate(app,db)
    
    
    jwt=JWTManager(app)
    api=Api(app)
    
    api.add_namespace(weatherNameSpace)
    

 
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )
        
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
        jsonify({"message": "The token has expired.", "error": "token_expired"}),
        401,
    )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )
    
    return app