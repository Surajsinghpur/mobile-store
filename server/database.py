from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

def init_db(app):
    """
    Binds the database instance to the Flask app.
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()  # This will create tables based on your models
