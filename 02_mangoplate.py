import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import sys

#keyword = sys.argv[1]
keyword = '제주도'

url = f"https://www.mangoplate.com/search/{keyword}"

#크롬창 없이 실행 - gui 없이 실행
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--headless")  
# driver = webdriver.Chrome(options = chrome_options) # GUI 없이 런 / 크롬창 없이


driver = webdriver.Chrome() #크롬창 (실행 확인용) - 위


driver.get(url)

req = driver.page_source
soup = BeautifulSoup(req, "html.parser")
info_list = soup.find_all(name="div", attrs={"class":"info"}) # 가게명 주소

# 페이지 주소 저장
page_urls = []
page_url_base = "https://www.mangoplate.com" # 기본주소 + href 

for info in info_list:
    review_url = info.find(name="a")
    if review_url is not None:
        page_urls.append(page_url_base + review_url.get("href")) # 가게 상세 페이지 url 생성

# 상위 5개 url 크롤링
titles = []
total_scores = []
addresses = []
menus = []

for url in page_urls[0:5]:
    driver.get(url)
    # 가게명
    element = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > header > div.restaurant_title_wrap > span > h1' #copy selector
    title_raw = driver.find_element(By.CSS_SELECTOR, element) # 엘레멘트 안의 셀렉터를 이용해서 값 추출
    title = title_raw.text # 값을 텍스트로 변경
    titles.append(title) # 리스트에 저장
    # 평점
    element = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > header > div.restaurant_title_wrap > span > strong > span'
    total_raw = driver.find_element(By.CSS_SELECTOR, element)
    total_score = total_raw.text
    total_scores.append(total_score)
    # 상세 주소
    element = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(1) > td > span.Restaurant__InfoAddress--Text'
    total_raw = driver.find_element(By.CSS_SELECTOR, element)
    address = total_raw.text
    addresses.append(address)

    # 대표 메뉴
    from selenium.common.exceptions import NoSuchElementException

    element1 = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(2) > td > span'
    element2 = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(3) > td > span'

    try:
        total_raw = driver.find_element(By.CSS_SELECTOR, element1)
    except NoSuchElementException:
        try:
            total_raw = driver.find_element(By.CSS_SELECTOR, element2)
        except NoSuchElementException:
            total_raw = None

    if total_raw:
        menu = total_raw.text
        menus.append(menu)


driver.quit()  # 크롬 드라이버 종료

# 데이터 프레임으로 변환
data = {
    'Title': titles,
    'Total Score': total_scores,
    'Address': addresses,
    'Menu': menus
}
df = pd.DataFrame(data)

# csv로 저장
file_name = 'mango_data.csv'
df.to_csv(file_name,index=False, encoding = 'utf-8-sig')

print(df)