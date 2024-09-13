from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

    
class Dataset(db.Model):
    __tablename__ = 'dataset'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    processed_at = db.Column(db.DateTime, default=None)  # Timestamp field
    status = db.Column(db.String(50), nullable=False, default='pending')

    def __init__(self, name, processed_at=None, status='pending'):
        self.name = name
        self.processed_at = processed_at
        self.status = status
