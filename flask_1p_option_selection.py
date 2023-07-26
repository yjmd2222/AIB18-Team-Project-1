from flask import Blueprint, render_template, request, jsonify
from flask_page_template_settings import options

bp = Blueprint('1페이지', __name__, url_prefix='/1페이지')

@bp.route('/', methods=['GET'])
def page_1():
    return render_template('firstTemplate.html', options=options)
