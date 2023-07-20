import sys
import os
import pandas as pd
import numpy as np
import sqlite3
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

driver.get('https://hotel.naver.com/hotels/main')
time.sleep(4)

keyword = '제주도'

keyword = '제주도'

element =driver.find_element(By.CLASS_NAME, 'SearchBox_btn_location__49Pk3')
time.sleep(4)
element.send_keys(Keys.ENTER)
time.sleep(4)
element2 =driver.find_element(By.CLASS_NAME, 'Autocomplete_txt__nb6wT')
element2.send_keys(keyword)
time.sleep(2)
driver.find_element(By.CLASS_NAME,"SearchResults_anchor__luLYP").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"SearchBox_search__tLThj").click()

name_list = []
id_list = []
rating_list = []
price_list = []

page = 5

try:
    for i in range(0, page):

        hotel_name_raw = driver.find_elements_by_css_selector('.name_area .name.ng-binding')
        for hotel_name in hotel_name_raw:
            i = hotel_name.text
            name_list.append(i)
        time.sleep(1)

        rating_raw = driver.find_elements_by_css_selector('.rating_area .score.ng-binding')
        for rating in rating_raw:
            i = rating.text
            rating_list.append(i)
        time.sleep(1)

        price_raw = driver.find_elements_by_css_selector('.lowest_price .price.ng-binding')
        for price in price_raw:
            i = price.text.replace('원', '').replace(',', '').replace('~', '')
            price_list.append(i)
        time.sleep(1)

        hotel_ids = driver.find_elements_by_css_selector('.hotel_item')
        for hotel_id in hotel_ids:
            hotel = hotel_id.get_attribute('data-hotelid')
            id_list.append(hotel)
        time.sleep(1)

        print(len(name_list), len(rating_list), len(price_list), len(id_list))

        driver.find_element_by_css_selector('.pagination .next').click()
        time.sleep(3)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

df = pd.DataFrame({'hotel_name': name_list, 'rating': rating_list, 'price': price_list, 'url_id': id_list})

conn = sqlite3.connect('hotel.db')

df.to_sql('people', conn, if_exists='replace', index=False)

conn.close()
