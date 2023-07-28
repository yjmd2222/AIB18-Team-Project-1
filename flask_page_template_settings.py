def money_first(list_: list):
    '리스트에서 금전상황 먼저 오도록 재정렬'
    return list_[-1:] + list_[:-1]

# A = [1,2,3,4,5]
# B = [2,4,1,3,0]

# print(sorted(A, key = lambda i: B.index(i)))




travel_item_list_db = ['항공권', '호텔', '렌터카']
travel_item_list_disp = ['항공권', '숙박시설', '렌터카']
travel_item_emojis = ['✈️', '🏨', '🚗']
travel_item_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(travel_item_list_disp, travel_item_list_db)}
travel_item_order_by_list = ['adult_charge', 'ratings', 'ratings']
travel_item_order_by_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(travel_item_list_db, travel_item_order_by_list)} # 다른 것과 다르게 key db

#  <항공권>

flight_columns_db = ['금전_상황', 'departure_kor','name' ]
flight_columns_disp = [ '금전상황', '출발공항', '항공사']
# flight_columns_db = money_first(flight_columns_db)
# flight_columns_disp = money_first(flight_columns_disp)

# <호텔>

hotel_columns_db = ['금전_상황', 'region', 'capacity' ]
hotel_columns_disp = ['금전상황', '지역','인원수' ]
# hotel_columns_db = money_first(hotel_columns_db)
# hotel_columns_disp = money_first(hotel_columns_disp)

# <렌터카>

car_columns_db = [ '금전_상황', 'age_req', 'size', 'seats','brand_name', 'fuel_type', 'transmission_type', 'driving_experience']
car_columns_disp = ['금전상황', '나이제한', '차종', '인승', '브랜드', '연료', '오토/스틱', '운전경력' ]
# car_columns_db = money_first(car_columns_db)
# car_columns_disp = money_first(car_columns_disp)
flight_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(flight_columns_disp,flight_columns_db)}
hotel_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(hotel_columns_disp,hotel_columns_db)}
car_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(car_columns_disp,car_columns_db)}
all_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(travel_item_list_disp, (flight_columns_kv, hotel_columns_kv, car_columns_kv))}
flight_values = [
    ['자린고비', '플렉스', '평범', '가성비', '욜로'],
    ['김포', '부산', '광주', '무안', '대구', '여수', '울산', '원주', '청주', '포항'],
    ['에어서울', '진에어', '이스타항공', '아시아나항공', '제주항공', '대한항공', '티웨이항공', '에어부산', '하이에어', '에어로케이']
    
    
]
# flight_values = money_first(flight_values)
hotel_values = [
    ['자린고비', '욜로', '평범', '플렉스', '가성비'],
    ['성산읍, 서귀포', '서귀포시, 서귀포', '서귀포', '제주 시내, 제주', '제주', '한림읍, 제주', '안덕면, 서귀포', '남원읍, 서귀포', '중문 해수욕장, 서귀포', '조천읍, 제주', '대정읍, 서귀포', '애월읍, 제주', '표선면, 서귀포', '우도, 제주', '구좌읍, 제주', '한경면, 제주'],
    [1, 2, 3, 4]
    
    
]
# hotel_values = money_first(hotel_values)
car_values = [
    ['자린고비', '가성비', '평범', '욜로', '플렉스'],
    [26, 24, 23, 22, 21, 25, 30],
    ['승합', '경차', '중소형', '전기', '중형', 'SUV', '고급', '수입'],
     [12, 5, 9, 7, 11, 8, 4, 6, 2, 15, 3, 13],
    ['현대', '기아', '르노코리아', '쉐보레', '쌍용', '푸조', 'BMW', '지프', '테슬라', '폭스바겐', '벤츠', '포드', '볼보', '아우디', '시트로앵', '캐딜락'],
    ['경유', '휘발유', '전기', 'LPG', '하이브리드'],
    ['오토', '스틱'],
    [1, 2, 3]
    
]
# car_values = money_first(car_values)

options = {travel_item: {} for travel_item in travel_item_list_disp}
for tdx, tuple_ in enumerate(zip((flight_columns_disp, hotel_columns_disp, car_columns_disp), (flight_values, hotel_values, car_values))):
    for cdx in range(len(tuple_[0])): # column idx
        options[travel_item_list_disp[tdx]][tuple_[0][cdx]] = tuple_[1][cdx]

# print(options)
# print(all_columns_kv)

flight_additional_options = {
    '성인': [1,2,3,4],
    '아동': [1,2,3,4],
    '편도/왕복': ['편도', '왕복']
}
