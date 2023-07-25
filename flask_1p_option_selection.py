from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('1페이지', __name__, url_prefix='/1페이지')

# 항공권, 렌트카, 호텔에 해당하는 서브 메뉴 이름을 딕셔너리로 준비합니다.
parent_menus = ['항공권', '렌트카', '호텔']
sub_menus = ['서브 메뉴'+str(i) for i in range(1,3+1)] # parent_values
sub_values = ['옵션'+str(i) for i in range(1,3+1)]

sub_menu_names = {
    parent_key: {parent_key + parent_value: [parent_key + parent_value + sub_value for sub_value in sub_values] for parent_value in sub_menus} for parent_key in parent_menus
}

@bp.route('/', methods=['GET'])
def page_1():
    return render_template('firstTemplate.html', sub_menu_names=sub_menu_names)
