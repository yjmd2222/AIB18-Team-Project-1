import time
import traceback
import csv

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup

from itertools import combinations

def parse_date(date_: datetime):
    '''datetime 'yyyy-mm-dd' 형식 str으로 반환'''
    return date_.strftime(r"%Y-%m-%d")

def rentcar_crawl(s_date_obj: datetime, e_date_obj: datetime, s_time='12:00', e_time='12:00'):
    '입력한 시간/날짜에 따라 크롤링 진행'
    driver.get('https://www.jeju.com/item/ren_meta.html?agt=jeju')

    s_date = parse_date(s_date_obj)
    e_date = parse_date(e_date_obj)

    print(f'{s_date}에서 {e_date} 렌트 조회시작')

    # sleep
    time.sleep(5)

    # 날짜 선택
    date_1 = driver.find_element(By.CLASS_NAME, 'date-selector')
    date_1.click()
    time.sleep(0.5)

    # 시작일
    date_1 = driver.find_element(By.XPATH, rf'//*[@title="{s_date}"]')
    date_1.click()
    time.sleep(0.5)

    # 종료일
    date_2 = driver.find_element(By.XPATH, rf'//*[@title="{e_date}"]')
    date_2.click()
    time.sleep(0.5)

    # 시작 시각
    rent_time = driver.find_elements(By.NAME, 'shm')[1]
    rent_time_select = Select(rent_time)
    rent_time_select.select_by_value(s_time)
    time.sleep(0.5)

    # 종료 시각
    return_time = driver.find_elements(By.NAME, 'ehm')[1]
    return_time_select = Select(return_time)
    return_time_select.select_by_value(e_time)
    time.sleep(0.5)

    # 적용하기 클릭
    done = driver.find_element(By.ID, 'btn_apply_date')
    done.click()
    time.sleep(0.5)

    # 가격 비교하기 클릭
    done = driver.find_element(By.CLASS_NAME, 'btn-search')
    done.click()
    time.sleep(5)

    # 각 차량마다 더보기 클릭
    more = driver.find_elements(By.CLASS_NAME, 'dummy-text')
    for i in more:
        i.click()
        time.sleep(0.01)

    # html parse
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #전체 결과 block
    prod_list = soup.select('#dummy_prd_list section')

    rentcar_csv(prod_list, s_date, e_date)

def get_date_combinations(start_date, days=30):
    'start_date부터 days일 후까지 가능한 시작/종료일 조합'
    date_list = []
    for i in range(days):
        current_date = start_date + timedelta(days=i)
        date_list.append(current_date)
    
    combinations_list = list(combinations(date_list, 2))
    return combinations_list

# csv 칼럼이름
columns = ['car_name', 'brand_name', 'seats', 'size', 'fuel_type', 'transmission_type', 'rental_company_name', 'age_req', 'driving_experice', 'year', 'ratings', 'price', 'start_date', 'end_date']

def rentcar_csv(prod_list, s_date, e_date):
    'csv로 저장'
    file_name = 'cars.csv'
    file_exists = False

    # 이미 파일 있으면 추가하기 위한 작업
    try:
        with open(file_name, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            file_exists = any(row for row in reader) # 파일에 데이터가 있는지 확인합니다.
    except FileNotFoundError:
        pass

    '''
<section id="prdno_RC522">
  <div class="rental-car-info">
    <img class="thumb" src="//jtns1.jeju.com/images/upload/contents/rc/787_rc_con.jpg" alt="더뉴K5">
    <dl>
      <dt class="car-name">
        <b>더뉴K5</b>
        <small>기아</small>
      </dt>
      <dd class="additional-info">
        <span>
          <i class="ico-people"></i>5인승 </span>
        <span>
          <i class="ico-car"></i>중형 </span>
        <span>
          <i class="ico-fuel"></i>LPG </span>
        <span>
          <i class="ico-gear"></i>오토 </span>
      </dd>
    </dl>
    <div class="price-info">
      <del>174,000</del>
      <br>
      <div class="flex-gap-7">
        <span class="insurance on">고급자차포함</span>
        <b>41,100원</b>
      </div>
    </div>
  </div>
  <table class="rental-company-list">
    <caption>렌터카 업체 목록</caption>
    <colgroup>
      <col style="width: 180px;">
      <col>
      <col>
      <col>
      <col>
      <col>
    </colgroup>
    <thead>
      <tr>
        <th scope="col">대여업체</th>
        <th scope="col">나이/경력</th>
        <th scope="col">연식</th>
        <th scope="col">편의 및 옵션</th>
        <th scope="col">가능대수</th>
        <th scope="col">
          <button type="button" class="btn-sort">평점(리뷰)</button>
        </th>
        <th scope="col">
          <button type="button" class="btn-sort up">대여료</button>
        </th>
      </tr>
    </thead>
    <tbody>
      <tr id="tr_RC522_hyundai">
        <td>
          <div class="form-check">
            <input type="checkbox" name="chk_compare[]" id="chk_RC522_hyundai" value="RC522@hyundai">
            <label class="label-compare hide" for="chk_RC522_hyundai">
              <em>상품비교함 담기</em>
            </label>
            <label class="">
              <button type="button" class="btn-detail">현대렌트카</button>
              <span class="badge hide">쿠폰</span>
            </label>
          </div>
        </td>
        <td>
          <button type="button" class="btn-detail">만22세/1년이상</button>
        </td>
        <td>
          <button type="button" class="btn-detail">19</button>
        </td>
        <td>
          <div class="benefit">
            <a href="#" class="btn-benefit" onclick="return false;">편의( <span>5</span>) / 옵션( <span>13</span>) </a>
            <dl class="layer-benefit">
              <dt>차량 옵션 및 편의 정보</dt>
              <dd>
                <ul class="option">
                  <li>· 금연</li>
                  <li>· 네비게이션</li>
                  <li>· 블루투스</li>
                  <li>· 후방센서</li>
                  <li>· 후방카메라</li>
                  <li>· 스마트키</li>
                  <li>· 열선시트</li>
                  <li>· 에어백</li>
                  <li>· 블랙박스</li>
                  <li>· 열선핸들</li>
                  <li>· 전동트렁크</li>
                  <li>· AUX</li>
                  <li>· USB</li>
                </ul>
                <ul class="convenience">
                  <li>· 낚시용품 지참가능</li>
                  <li>· 새벽반납 무료</li>
                  <li>· 안심살균렌터카</li>
                  <li>· 전차량 금연</li>
                  <li>· 전차량 후방카메라</li>
                </ul>
                <em>* 옵션은 실시간 반영이 아니므로 차이가 있을 수 있습니다. 필수 희망 옵션은 업체로 문의 바랍니다.</em>
              </dd>
            </dl>
          </div>
        </td>
        <td>
          <span class="count">1</span>
        </td>
        <td>
          <div class="ratings">
            <i class="ico-star"></i>3.7 <span class="fc-lightgray">(11)</span>
          </div>
        </td>
        <td class="price-group">
          <button class="price btn-detail">41,100</button>
          <span class="tooltip">최저가 보장 업체</span>
        </td>
      </tr>
    ...
</section>
    '''
    data_list = []
    rental_dates = [s_date, e_date]
    for section in prod_list:
        car_name = section.select_one('.car-name b').text.strip()
        brand_name = section.select_one('.car-name small').text.strip()
        seats = section.select_one('.ico-people').next_sibling.strip()
        size = section.select_one('.ico-car').next_sibling.strip()
        fuel_type = section.select_one('.ico-fuel').next_sibling.strip()
        transmission_type = section.select_one('.ico-gear').next_sibling.strip()
        rental_companies = section.select_one('.rental-company-list tbody')
        for company in rental_companies:
            rental_company_name = company.contents[0].find('button').text.strip()
            age_req, driving_experience = company.contents[1].find('button').text.strip().split('/')
            year = company.contents[2].find('button').text.strip()
            ratings = float(company.contents[5].select_one('.ico-star').next_sibling.strip())
            price = int(company.contents[6].find('button').text.strip().replace(',',''))
            data_list.append([car_name,
                              brand_name,
                              seats,
                              size,
                              fuel_type,
                              transmission_type,
                              rental_company_name,
                              age_req,
                              driving_experience,
                              year,
                              ratings,
                              price]
                              + rental_dates)

    with open('cars.csv', 'a+', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        if not file_exists:
            csv_writer.writerow(columns)
        csv_writer.writerows(data_list)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()

    s_date = datetime.today() + timedelta(days=1)
    date_combos = get_date_combinations(s_date)

    # rentcar_crawl(date_combos[5][0], date_combos[5][1])

    for combo in date_combos:
        rentcar_crawl(combo[0], combo[1])

    driver.quit()