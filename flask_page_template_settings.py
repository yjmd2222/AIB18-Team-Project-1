# 항공권, 렌트카, 호텔에 해당하는 서브 메뉴 이름을 딕셔너리로 준비합니다.
travel_item_list = ['항공권', '렌터카', '호텔']
flight_columns_db = ['name', 'seat', 'departure_kor', 'direction', '금전_상황']
flight_columns_disp = ['항공사', '좌석개수', '출발공항', '가는편', '금전 상황']
car_columns_db = ['brand_name', 'seats', 'size', 'fuel_type', 'transmission_type', 'rental_company_name', 'age_req', 'driving_experience', 'year', '금전_상황']
car_columns_disp = ['브랜드', '좌석개수', '사이즈', '연료', '오토/스틱', '렌터카 회사', '나이제한', '운전경력', '연식', '금전 상황']
hotel_columns_db = ['capacity', '금전_상황']
hotel_columns_disp = ['인원수', '금전 상황']
flight_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(flight_columns_db,flight_columns_disp)}
car_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(car_columns_db,car_columns_disp)}
hotel_columns_kv = {tuple_[0]: tuple_[1] for tuple_ in zip(hotel_columns_db,hotel_columns_disp)}
flight_values = [
    ['에어서울', '진에어', '이스타항공', '아시아나항공', '제주항공', '대한항공', '티웨이항공', '에어부산', '하이에어', '에어로케이'],
    ['특가석', '할인석', '일반석', '특가석-환불불가', '특가석-수하물유료'],
    ['김포', '제주', '부산', '광주', '무안', '대구', '여수', '울산', '원주', '청주', '포항'],
    ['come', 'back'],
    ['자린고비', '플렉스', '평범', '가성비', '욜로']
]
car_values = [
    ['현대', '기아', '르노코리아', '쉐보레', '쌍용', '푸조', 'BMW', '지프', '테슬라', '폭스바겐', '벤츠', '포드', '볼보', '아우디', '시트로앵', '캐딜락'],
    [12, 5, 9, 7, 11, 8, 4, 6, 2, 15, 3, 13],
    ['승합', '경차', '중소형', '전기', '중형', 'SUV', '고급', '수입'],
    ['경유', '휘발유', '전기', 'LPG', '하이브리드'],
    ['오토', '스틱'],
    ['다움렌트카', '굿모닝렌트카', '로그인렌트카', '무지개렌트카', '퍼스트렌트카', '에이스렌트카', '패밀리렌트카', '씨유렌트카', '스마트렌트카', '갤럭시렌터카', '퍼시픽렌트카', '제주공항렌트카', '한라산렌트카', '보고타렌트카', '제주OK렌터카', '한국렌트카', '드림렌트카', '매일렌트카', 'KD렌트카', '레인보우모빌리티', '오렌지렌트카', '용두암렌트카', '썬렌트카', '현대렌트카', '제주사랑렌트카', '땡큐제주 렌트카', '메트로렌트카', '아산렌트카', '평화렌트카', '제주마음렌트카', '더세븐렌트카', '자유렌트카', '바로렌트카', '대한렌트카'],
    [26, 24, 23, 22, 21, 25, 30],
    [1, 2, 3],
    ['19', '18~19', '20', '18~20', '17~20', '19~21', '18', '21', '19~20', '22', '21~22', '17~18', '16~17', '15~16', '16', '20~22', '20~21', '20~23', '17~19', '17', '15~18', '16~18', '14~18', '15~17', '23', '21~23', '22~23', '15', '19~22', '14~17', '16~19', '16~20'],
    ['자린고비', '가성비', '평범', '욜로', '플렉스', None]
]
hotel_values = [
    [1, 2, 3, 4],
    ['자린고비', '욜로', '평범', '플렉스', '가성비']
]

options = {travel_item: {} for travel_item in travel_item_list}
for tdx, tuple_ in enumerate(zip((flight_columns_disp, car_columns_disp, hotel_columns_disp), (flight_values, car_values, hotel_values))):
    for cdx in range(len(tuple_[0])): # column idx
        options[travel_item_list[tdx]][tuple_[0][cdx]] = tuple_[1][cdx]