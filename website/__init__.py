from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)
    
    # Initialize Bootstrap for the app
    Bootstrap5(app)
    
    # Set the secret key for the app
    app.secret_key = 'somesecretgoeshere'
    
    # Configure the SQLAlchemy database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website4143.sqlite'
    
    # Initialize the SQLAlchemy database with the app
    db.init_app(app)

    # Define the upload folder for static files
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Initialize the LoginManager for user authentication
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Set the login view
    login_manager.init_app(app)

    # Define a user loader function for LoginManager
    from .models import User  # Import the User model
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints for different parts of the application
    from . import views
    app.register_blueprint(views.mainbp)  # Main Blueprint
    from . import events
    app.register_blueprint(events.bp)  # Events Blueprint
    from . import auth
    app.register_blueprint(auth.bp)  # Authentication Blueprint
    

    return app
