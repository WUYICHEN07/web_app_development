from datetime import datetime

# 根據系統架構，db 定義於 app/__init__.py
from app import db # 或者從其他的 db instance 導入

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=True)
    publisher = db.Column(db.String(255), nullable=True)
    publish_date = db.Column(db.String(50), nullable=True)
    isbn = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    reviews = db.relationship('Review', backref='book', lazy=True, cascade="all, delete-orphan")
    comments = db.relationship('Comment', backref='book', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Book {self.title}>"

    @classmethod
    def create(cls, **kwargs):
        book = cls(**kwargs)
        db.session.add(book)
        db.session.commit()
        return book

    @classmethod
    def len(cls):
        return cls.query.count()
        
    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, book_id):
        return cls.query.get(book_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
