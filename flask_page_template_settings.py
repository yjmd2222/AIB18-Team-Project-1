# 항공권, 렌트카, 호텔에 해당하는 서브 메뉴 이름을 딕셔너리로 준비합니다.
travel_item_list = ['항공권', '호텔', '렌터카']
travel_item_list_disp = ['항공권', '숙박시설', '렌터카']
flight_columns_db = ['name', 'departure_kor', 'direction', '금전_상황']
flight_columns_disp = ['항공사', '출발공항', '가는편', '금전상황']
hotel_columns_db = ['capacity', '금전_상황']
hotel_columns_disp = ['인원수', '금전상황']
car_columns_db = ['brand_name', 'seats', 'size', 'fuel_type', 'transmission_type', 'age_req', 'driving_experience', '금전_상황']
car_columns_disp = ['브랜드', '인승', '차종', '연료', '오토/스틱', '나이제한', '운전경력', '금전상황']
flight_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(flight_columns_disp,flight_columns_db)}
hotel_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(hotel_columns_disp,hotel_columns_db)}
car_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(car_columns_disp,car_columns_db)}
all_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(travel_item_list, (flight_columns_kv, hotel_columns_kv, car_columns_kv))}
flight_values = [
    ['에어서울', '진에어', '이스타항공', '아시아나항공', '제주항공', '대한항공', '티웨이항공', '에어부산', '하이에어', '에어로케이'],
    ['김포', '제주', '부산', '광주', '무안', '대구', '여수', '울산', '원주', '청주', '포항'],
    ['come', 'back'],
    ['자린고비', '플렉스', '평범', '가성비', '욜로']
]
hotel_values = [
    [1, 2, 3, 4],
    ['자린고비', '욜로', '평범', '플렉스', '가성비']
]
car_values = [
    ['현대', '기아', '르노코리아', '쉐보레', '쌍용', '푸조', 'BMW', '지프', '테슬라', '폭스바겐', '벤츠', '포드', '볼보', '아우디', '시트로앵', '캐딜락'],
    [12, 5, 9, 7, 11, 8, 4, 6, 2, 15, 3, 13],
    ['승합', '경차', '중소형', '전기', '중형', 'SUV', '고급', '수입'],
    ['경유', '휘발유', '전기', 'LPG', '하이브리드'],
    ['오토', '스틱'],
    [26, 24, 23, 22, 21, 25, 30],
    [1, 2, 3],
    ['자린고비', '가성비', '평범', '욜로', '플렉스']
]

print(all_columns_kv)

options = {travel_item: {} for travel_item in travel_item_list}
for tdx, tuple_ in enumerate(zip((flight_columns_disp, hotel_columns_disp, car_columns_disp), (flight_values, hotel_values, car_values))):
    for cdx in range(len(tuple_[0])): # column idx
        options[travel_item_list[tdx]][tuple_[0][cdx]] = tuple_[1][cdx]