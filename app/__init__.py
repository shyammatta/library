from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

        from .models import User, Book
        if not User.query.first():
            initial_users = [
                {'username': 'shyam', 'password': 'shyam'},
                {'username': 'rithika', 'password': 'rithika'},
                {'username': 'rushik', 'password': 'rushik'},
                {'username': 'saraswathi', 'password': 'saraswathi'}
            ]
            for user_data in initial_users:
                user = User(username=user_data['username'], password=user_data['password'])
                db.session.add(user)
            db.session.commit()

        if not Book.query.first():
            initial_books = [
                {'name': 'House of Leaves'},
                {"name": "Rosemary's Baby"},
                {'name': 'Night Film'},
                {"name": "Daddy's Boy"},
                {'name': 'Bossypants'},
                {'name': 'Yes Please'},
                {'name': 'Sherlock Holmes'},
                {'name': 'Dark Matter'},
                {'name': 'Gone Girl'},
                {'name': 'The Fury'},
                {'name': 'A Little Life'},
                {'name': 'The Exchange'}
            ]
            for book_data in initial_books:
                book = Book(name=book_data['name'])
                db.session.add(book)
            db.session.commit()

    return app
