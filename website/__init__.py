from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import datetime

db=SQLAlchemy()

def create_app():
    
    app=Flask(__name__)
    
    Bootstrap5(app)
  
    app.secret_key='somesecretgoeshere'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///website1153.sqlite'
    db.init_app(app)
    
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER    

    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

  #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import events
    app.register_blueprint(events.bp)
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app



