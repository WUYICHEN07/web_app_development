from flask import Blueprint, request, redirect, url_for, flash

comments_bp = Blueprint('comments', __name__, url_prefix='/comments')

@comments_bp.route('/<int:book_id>', methods=['POST'])
def create_comment(book_id):
    """
    HTTP POST /comments/<book_id>
    接收留言表單資料（若是回覆則需包含 parent_id），儲存至資料庫後重導向回書籍詳細頁。
    """
    pass
