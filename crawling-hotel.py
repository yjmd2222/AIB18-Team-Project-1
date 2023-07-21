import csv

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

from itertools import combinations

columns = ['hotel_name','region','ratings', 'price', 'start_date', 'end_date']

def parse_date(date_: datetime):
    '''datetime 'yyyy-mm-dd' 형식 str으로 반환'''
    return date_.strftime(r"%Y-%m-%d")

def hotel_crawl(s_date: datetime, e_date: datetime):
    '입력한 시간/날짜에 따라 크롤링 진행'
    print(f'{s_date}에서 {e_date} 숙박 조회시작')

    s_date = parse_date(s_date)
    e_date = parse_date(e_date)

    try:
        # 날짜 선택 박스
        date_selector = driver.find_element(By.CLASS_NAME, 'b91c144835')
        date_selector.click()

        # 시작일
        date_1 = driver.find_element(By.XPATH, rf'//*[@data-date="{s_date}"]')
        date_1.click()

        # 종료일
        date_2 = driver.find_element(By.XPATH, rf'//*[@data-date="{e_date}"]')
        date_2.click()

        # 적용하기 클릭
        done = driver.find_element(By.XPATH, r'//*[@type="submit"]')
        done.click()
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        prod_list = soup.select('.a826ba81c4.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942')
    except Exception as error:
        print(f'에러: {type(error).__name__}, 메시지: {error}')
    hotel_csv(prod_list, s_date, e_date)

def get_date_combinations(start_date, days=30):
    'start_date부터 days일 후까지 가능한 시작/종료일 조합'
    date_list = []
    for i in range(days):
        current_date = start_date + timedelta(days=i)
        date_list.append(current_date)
    
    combinations_list = list(combinations(date_list, 2))
    return combinations_list

def hotel_csv(prod_list, s_date, e_date):
    'csv로 저장'
    file_name = 'hotels.csv'
    file_exists = False

    # 이미 파일 있으면 추가하기 위한 작업
    try:
        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            file_exists = any(row for row in reader) # 파일에 데이터가 있는지 확인합니다.
    except FileNotFoundError:
        pass


    data_list = []
    stay_length_dates = [s_date, e_date]
    for section in prod_list:
        hotel_name = section.select_one('[data-testid="title"]').text.strip()
        region = section.select_one('[data-testid="address"]').text.strip()
        ratings = float(section.select_one('.b5cd09854e.d10a6220b4').text.strip())
        price = int(section.select_one('[data-testid="price-and-discounted-price"]').text.strip().replace(',','').replace('₩',''))
        data_list.append([hotel_name,
                            region,
                            ratings,
                            price]
                            + stay_length_dates)

    with open('hotel.csv', 'a+', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file, delimiter=';')
        if not file_exists:
            csv_writer.writerow(columns)
        csv_writer.writerows(data_list)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(r'https://www.booking.com/searchresults.ko.html?ss=%EC%A0%9C%EC%A3%BC%EB%8F%84%2C+%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&label=gen173nr-1FCAQoggJCEHNlYXJjaF_soJzso7zrj4RIF1gEaH2IAQGYARe4ARfIAQzYAQHoAQH4AQOIAgGoAgO4At_456UGwAIB0gIkNjZjMzFmMjktN2Q2NC00ZGI3LThlZDAtNTkzYWUzZWExNzNh2AIF4AIB&sid=14dedff24ad71b3922a2f34073ee4036&aid=304142&lang=ko&sb=1&src_elem=sb&src=index&dest_id=4170&dest_type=region&checkin=2023-07-20&checkout=2023-07-21&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure')
    driver.implicitly_wait(3)

    s_date = datetime.today() + timedelta(days=1)
    date_combos = get_date_combinations(s_date)

    for combo in date_combos:
        hotel_crawl(combo[0], combo[1])

    driver.quit()

    