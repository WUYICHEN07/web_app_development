from flask import Blueprint, render_template

ranking_bp = Blueprint('ranking', __name__, url_prefix='/ranking')

@ranking_bp.route('/', methods=['GET'])
def list_ranking():
    """
    HTTP GET /ranking/
    查詢資料庫，計算所有書籍平均評分，依平均評分由高至低排序，顯示推薦排行榜頁面。
    """
    pass
