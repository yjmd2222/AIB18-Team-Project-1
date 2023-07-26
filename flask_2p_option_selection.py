from flask import Blueprint, render_template, request, json
from flask_page_template_settings import travel_item_list_kv, all_columns_kv

bp = Blueprint('2페이지', __name__, url_prefix='/2페이지')

def page_2_wrap_other_funcs(json_data_raw:dict):
    '하나의 함수로 병합'
    def unfoil_inner_json(travel_item, json_data_inner:list):
        'json 안에 호텔,렌트카,항공권 개별 데이터 처리'
        # 솔직히 리스트였으면 아래 스텝 하나 필요 없음
        list_ = [list(item.values()) for item in json_data_inner] # [[칼럼명,값],...]
        print(list_)
        list_ = [[all_columns_kv[travel_item][item[0]],item[1]] for item in list_] # [[sql_칼럼명,값],...]
        list_ = [' == \''.join(item)+'\'' for item in list_] # ['칼럼명 == \'값\'',...]
        return ' AND '.join(list_) # '칼럼명1 == \'값1\' AND 칼럼명2 == \'값2\',...'

    def unfoil_outer_json(json_data_whole:dict):
        '전체 json 데이터 정리해서 where문 안에 들어갈 str들로 반환'
        from datetime import datetime

        dict_ = {travel_item: [''] for travel_item in list(travel_item_list_kv.values())}
        # print(json_data_whole.items())
        for k, v in json_data_whole.items():
            # 항공권, 렌트카, 호텔이라면
            if k != 'dateRange':
                # list로 감싸서 str 저장. 항공권의 경우 datetime append해야 함
                dict_[travel_item_list_kv[k]] = [unfoil_inner_json(k, v)]
                # 결과 형태: {'호텔': ['col1 == value1 AND col2 == value2... AND end_date == \'2023-07-09 00:00:00\''],...}
                # 항공권: ['col1 == value1...', (start_date, end_date)]
            # 날짜라면
            else:
                # 날짜 추가해야함
                start_date, end_date = v.split(' - ')
                print(start_date, end_date)
                # 항공권만 칼럼 이름 다름
                start_date = datetime.strptime(start_date, r'%m/%d/%Y')
                end_date = datetime.strptime(end_date, r'%m/%d/%Y')
                start_date_flight = start_date.strftime(r'%Y-%m-%d')
                end_date_flight = end_date.strftime(r'%Y-%m-%d')
                start_date_else = start_date.strftime(r'%Y-%m-%d %H:%M:%S')
                end_date_else = end_date.strftime(r'%Y-%m-%d %H:%M:%S')
                where_date_part = f'start_date == \'{start_date_else}\' AND end_date == \'{end_date_else}\''
                for k_ in dict_:
                    if k_ != list(travel_item_list_kv)[0]:
                        if dict_[k_][0]:
                            where_date_part_ = ' AND ' + where_date_part
                        else:
                            where_date_part_ = where_date_part
                        dict_[k_][0] += where_date_part_
                    else:
                        dict_[k_].append((start_date_flight, end_date_flight))
        return dict_

    def return_select_sqls(where_dict):
        'sql문 반환'

        # sql 내에서 계산할 것이 아니라 python에서 계산한다면
        # 가는 표 오는 표 각각 필요할 듯
        # 1. 항공권
        flight_other_columns = where_dict[list(travel_item_list_kv.values())[0]][0]
        flight_where_to_jeju = f'arrival == \'CJU\' AND DATE(SUBSTR(departure_datetime, 1, 10)) == \'{where_dict[list(travel_item_list_kv.values())[0]][1][0]}\''
        flight_where_from_jeju = f'departure == \'CJU\' AND DATE(SUBSTR(departure_datetime, 1, 10)) == \'{where_dict[list(travel_item_list_kv.values())[0]][1][1]}\''
        if flight_other_columns:
            flight_where_to_jeju = ' AND ' + flight_where_to_jeju
            flight_where_from_jeju = ' AND ' + flight_where_from_jeju
        flight_where_to_jeju = flight_other_columns + flight_where_to_jeju
        flight_where_from_jeju = flight_other_columns + flight_where_from_jeju
        sql_select_flights_to_jeju = f"""
        SELECT *
        FROM {list(travel_item_list_kv.values())[0]}
        WHERE
        {flight_where_to_jeju}
        ORDER BY adult_charge
        LIMIT 3
        """
        sql_select_flights_from_jeju = f"""
        SELECT *
        FROM {list(travel_item_list_kv.values())[0]}
        WHERE
        {flight_where_from_jeju}
        ORDER BY adult_charge
        LIMIT 3
        """

        # 2. 렌터카
        sql_select_cars = f"""
        SELECT *
        FROM {list(travel_item_list_kv.values())[1]}
        WHERE
        {where_dict[list(travel_item_list_kv.values())[1]][0]}
        ORDER BY ratings DESC
        LIMIT 3
        """

        # 3. 호텔
        sql_select_hotels = f"""
        SELECT *
        FROM {list(travel_item_list_kv.values())[2]}
        WHERE
        {where_dict[list(travel_item_list_kv.values())[2]][0]}
        ORDER BY ratings DESC
        LIMIT 3
        """

        print(sql_select_cars)
        print(sql_select_hotels)
        print(sql_select_flights_to_jeju)
        print(sql_select_flights_from_jeju)

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
        # print("Received data:", data)
        print(page_2_wrap_other_funcs(json.loads(data)))

        return render_template('index.html')
