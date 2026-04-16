from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    """
    HTTP GET /
    渲染首頁，顯示系統簡介、排行榜摘要與本月新書摘要。
    """
    pass
