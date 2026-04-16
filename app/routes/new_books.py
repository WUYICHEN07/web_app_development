from flask import Blueprint, render_template

new_books_bp = Blueprint('new_books', __name__, url_prefix='/new-books')

@new_books_bp.route('/', methods=['GET'])
def list_new_books():
    """
    HTTP GET /new-books/
    篩選本月建立的書籍，以卡片形式顯示。
    """
    pass
