from flask import Blueprint, request, redirect, url_for, flash

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@reviews_bp.route('/<int:book_id>', methods=['POST'])
def create_review(book_id):
    """
    HTTP POST /reviews/<book_id>
    接收心得評分表單資料，儲存至資料庫後重導向回書籍詳細頁。
    """
    pass
