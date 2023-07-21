import csv

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

from itertools import combinations

columns = ['hotel_name','region','ratings', 'price', 'start_date', 'end_date']

def parse_date(date_: datetime):
    '''datetime 'yyyy-mm-dd' 형식 str으로 반환'''
    return date_.strftime(r"%Y-%m-%d")

def try_find_element_click(*args, click=True):
    '''
    셀레니움 element 찾고 click을 try-except wrapper로 구성\n
    *args: (by, value)들로 구성된 튜플 -> ((by, value),)
    '''
    while True:
        try:
            for tuple_ in args:
                print(tuple_)
                element = driver.find_element(*tuple_)
                if click:
                    element.click()
                else:
                    return element
            break
        except NoSuchElementException:
            print('팝업 종료')
            close_popup = driver.find_element(By.XPATH, r'//*[@aria-label="로그인 혜택 안내 창 닫기."]')
            close_popup.click()
    return None

def hotel_crawl(s_date: datetime, e_date: datetime):
    '입력한 시간/날짜에 따라 크롤링 진행'
    print(f'{s_date}에서 {e_date} 숙박 조회시작')

    s_date = parse_date(s_date)
    e_date = parse_date(e_date)

    # 날짜 박스 + 시작 + 종료일 클릭
    try_find_element_click((By.CLASS_NAME, 'b91c144835'), (By.XPATH, rf'//*[@data-date="{s_date}"]'), (By.XPATH, rf'//*[@data-date="{e_date}"]'))

    # 적용하기 클릭
    try_find_element_click((By.XPATH, r'//*[@type="submit"]'))
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # property-card 로딩 기다리기
    WebDriverWait(driver, 5)
    
    property_card = soup.select('.a826ba81c4.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942')

    hotel_csv(property_card, s_date, e_date)

def get_date_combinations(start_date, days=30):
    'start_date부터 days일 후까지 가능한 시작/종료일 조합'
    date_list = []
    for i in range(days):
        current_date = start_date + timedelta(days=i)
        date_list.append(current_date)
    
    combinations_list = list(combinations(date_list, 2))
    return combinations_list

def hotel_csv(soup_elements, s_date, e_date):
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
    print(stay_length_dates)
    for property_card in soup_elements:
        hotel_name = property_card.select_one('[data-testid="title"]').text.strip()
        region = property_card.select_one('[data-testid="address"]').text.strip()
        ratings = float(property_card.select_one('.b5cd09854e.d10a6220b4').text.strip())
        price = int(property_card.select_one('[data-testid="price-and-discounted-price"]').text.strip().replace(',','').replace('₩',''))
        data_list.append([hotel_name,
                            region,
                            ratings,
                            price]
                            + stay_length_dates)

    with open(file_name, 'a+', encoding='utf-8', newline='') as file:
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

    