from datetime import datetime

# 根據系統架構，db 定義於 app/__init__.py
from app import db

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id', ondelete='CASCADE'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id', ondelete='CASCADE'), nullable=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    replies = db.relationship(
        'Comment', backref=db.backref('parent', remote_side=[id]),
        lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Comment {self.id} for Book {self.book_id}>"

    @classmethod
    def create(cls, **kwargs):
        comment = cls(**kwargs)
        db.session.add(comment)
        db.session.commit()
        return comment

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, comment_id):
        return cls.query.get(comment_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
