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