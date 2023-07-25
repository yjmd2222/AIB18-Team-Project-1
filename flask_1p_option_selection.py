from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('1페이지', __name__, url_prefix='/1페이지')

# 항공권, 렌트카, 호텔에 해당하는 서브 메뉴 이름을 딕셔너리로 준비합니다.
travel_item_list = ['항공권', '렌터카', '호텔']
flight_columns = ['name', 'seat', 'departure_kor', '금전_상황']
car_columns = ['car_name', 'brand_name', 'seats', 'size', 'fuel_type', 'transmission_type', 'rental_company_name', 'age_req', 'driving_experience', 'year', 'ratings', '금전_상황']
hotel_columns = ['hotel_name', 'ratings', 'capacity', '금전_상황']

from sqlite3 import OperationalError

def get_connection():
    'connection obj return하는 함수'
    import sqlite3
    conn = sqlite3.connect('proj.db')

    return conn

flight_values = [

]

conn = get_connection()
cur = conn.cursor()
for idx, columns in enumerate((flight_columns, car_columns, hotel_columns)):
    travel_item = travel_item_list[idx]
    for col_name in columns:
        sql = f'select distinct {col_name} from {travel_item}'
        cur.execute(sql)
        rows = cur.fetchall()
        print(travel_item, col_name, [i[0] for i in rows])
cur.close()
conn.close()

# sub_menu_names = {
#     parent_key: {parent_key + parent_value: [parent_key + parent_value + sub_value for sub_value in sub_values] for parent_value in sub_menus} for parent_key in parent_menus
# }

@bp.route('/', methods=['GET'])
def page_1():
    return render_template('firstTemplate.html', sub_menu_names=sub_menu_names)
