from flask import Blueprint, render_template, request, redirect, url_for, flash

books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('/', methods=['GET'])
def list_books():
    """
    HTTP GET /books/
    顯示書籍列表，並支援依書名或作者進行搜尋。
    """
    pass

@books_bp.route('/new', methods=['GET'])
def create_book_page():
    """
    HTTP GET /books/new
    顯示新增書籍的表單頁面。
    """
    pass

@books_bp.route('/', methods=['POST'])
def create_book():
    """
    HTTP POST /books/
    接收表單資料，寫入資料庫並重導向至詳細頁面。
    """
    pass

@books_bp.route('/<int:id>', methods=['GET'])
def book_detail(id):
    """
    HTTP GET /books/<id>
    顯示單筆書籍的詳細資訊，包含心得列表與對話框。
    """
    pass

@books_bp.route('/<int:id>/edit', methods=['GET'])
def edit_book_page(id):
    """
    HTTP GET /books/<id>/edit
    顯示編輯書籍的表單，預填現有資料。
    """
    pass

@books_bp.route('/<int:id>/update', methods=['POST'])
def update_book(id):
    """
    HTTP POST /books/<id>/update
    接收表單資料，更新資料庫。
    """
    pass

@books_bp.route('/<int:id>/delete', methods=['POST'])
def delete_book(id):
    """
    HTTP POST /books/<id>/delete
    刪除指定書籍，重導向至列表頁。
    """
    pass
