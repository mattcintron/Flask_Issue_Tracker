# site built from examples taken from here -
# https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_issue_tracker.config import Config

# how to build the data base
# first open up the terminal than in the python shell write
# from flask import db
# then to create the db at this directory location
# db.create_all()
# to import Models
# from FlaskBlog import User, Post
# to add user
# user2 =User(username='Jhon', email='J@demo.com', password='password')
# db.session.add(user1)
# to commit changes
# db.session.commit()
# to query users
# User.query.all()
# User.query.first()
# User.query.filter_by(username='Matt').all()
# get user with id
# User.query.get(1)
# to make a post
#  post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
# to clear all data
# db.drop_all()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)


    # blueprints
    from flask_issue_tracker.users.routes import users
    from flask_issue_tracker.posts.routes import posts
    from flask_issue_tracker.main.routes import main
    from flask_issue_tracker.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app



