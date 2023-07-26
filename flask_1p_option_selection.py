from flask import Blueprint, render_template
from flask_page_template_settings import options, travel_item_emojis

bp = Blueprint('1페이지', __name__, url_prefix='/1페이지')

@bp.route('/', methods=['GET'])
def page_1():
    return render_template('firstTemplate.html', options=options, travel_item_emojis=travel_item_emojis)
