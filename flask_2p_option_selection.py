from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('2페이지', __name__, url_prefix='/2페이지')

# 항공권, 렌트카, 호텔에 해당하는 서브 메뉴 이름을 딕셔너리로 준비합니다.
parent_menus = ['항공권', '렌트카', '호텔']
sub_menus = ['서브 메뉴'+str(i) for i in range(1,3+1)] # parent_values
sub_values = ['옵션'+str(i) for i in range(1,3+1)]

sub_menu_names = {
    parent_key: {parent_key + parent_value: [parent_key + parent_value + sub_value for sub_value in sub_values] for parent_value in sub_menus} for parent_key in parent_menus
}

def page_1_wrap_other_funcs(json_data_raw:dict):
    '하나의 함수로 병합'
    def unfoil_inner_json(json_data_inner:list):
        'json 안에 호텔,렌트카,항공권 개별 데이터 처리'
        # 솔직히 리스트였으면 아래 스텝 하나 필요 없음
        list_ = [list(item.values()) for item in json_data_inner] # [[칼럼명,값],...]
        list_ = [' == '.join(item) for item in list_] # ['칼럼명 = :값',...]
        return ' AND '.join(list_) # '칼럼명1 = :값1 AND 칼럼명2 =: 값2,...'

    def unfoil_outer_json(json_data_whole:dict):
        '전체 json 데이터 정리해서 where문 안에 들어갈 str들로 반환'
        from datetime import datetime

        dict_ = {
            '항공권': None,
            '렌트카': None,
            '호텔': None
        }
        for idx, (k, v) in enumerate(json_data_whole.items()):
            # 항공권, 렌트카, 호텔이라면
            if idx != 3:
                # str 저장
                dict_[k] = unfoil_inner_json(v)
            # 날짜라면
            else:
                # 날짜 추가해야함
                start_date, end_date = v.split(' - ')
                start_date = datetime.strptime(start_date, r'%m/%d/%Y').strftime(r'%Y-%m-%d %H:%M:%S')
                end_date = datetime.strptime(end_date, r'%m/%d/%Y').strftime(r'%Y-%m-%d %H:%M:%S')
                where_date_part = f' AND start_date == {start_date} AND end_date == {end_date}'
                for k_ in dict_:
                    # 날짜 추가
                    dict_[k_] += where_date_part
        return dict_

    def return_select_sqls(where_dict):
        'sql문 반환'

        # 1. 렌트카
        sql_select_cars = f"""
        SELECT *
        FROM cars
        WHERE
        {where_dict['렌트카']}
        ORDER BY ratings DESC
        LIMIT 3
        """

        # 2. 호텔
        sql_select_hotels = f"""
        SELECT *
        FROM hotels
        WHERE
        {where_dict['호텔']}
        ORDER BY ratings DESC
        LIMIT 3
        """

        # sql 내에서 계산할 것이 아니라 python에서 계산한다면
        # 가는 표 오는 표 각각 필요할 듯
        # 3. 항공권
        flight_where_to_jeju = where_dict['항공권'] + ' AND arrival == CJU'
        flight_where_from_jeju = where_dict['항공권'] + ' AND departure == CJU'
        sql_select_flights_to_jeju = f"""
        SELECT *
        FROM hotels
        WHERE
        {flight_where_to_jeju}
        ORDER BY ratings DESC
        LIMIT 3
        """
        sql_select_flights_from_jeju = f"""
        SELECT *
        FROM hotels
        WHERE
        {flight_where_from_jeju}
        ORDER BY ratings DESC
        LIMIT 3
        """

        return sql_select_cars, sql_select_hotels, sql_select_flights_to_jeju, sql_select_flights_from_jeju

    def get_connection():
        'connection obj return하는 함수'
        import sqlite3
        conn = sqlite3.connect('proj.db')

        return conn

    def fetch_data(sql_select)->list:
        'DB에서 데이터 fetch하기'
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(sql_select)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return rows

    where_dict = unfoil_outer_json(json_data_raw)
    sqls = return_select_sqls(where_dict)

    keys = ['렌트카', '호텔', '항공권_to', '항공권_from']

    return {tuple_[0]: fetch_data(tuple_[1]) for tuple_ in zip(keys, sqls)}

@bp.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        # Get the data sent from the form
        data = request.form.get('input_data')
        print("Received data:", data)
        # Perform any additional processing or database operations with the data here

        return render_template('firstTemplate.html', sub_menu_names=sub_menu_names)
