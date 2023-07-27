import pandas as pd

df = pd.read_csv('weather_DB.csv', encoding='utf-8') 

def load_weather_data(selected_date):
    # Filter the DataFrame to get the weather data for the selected date
    selected_data = df[df['Day'] == selected_date]

    if selected_data.empty:
        print(f"No weather data found for selected date: {selected_date}")
        return None

    return selected_data

def main(start_date, end_date):
    # Convert start_date and end_date to integers representing the day of the month
    start_date = int(start_date.split('-')[2])
    end_date = int(end_date.split('-')[2])

    # Check if the end date is greater than or equal to the start date
    if end_date < start_date:
        return "End date should be greater than or equal to the start date."

    # Generate the list of selected dates within the date range
    selected_dates = list(range(start_date, end_date + 1))

    output = ""
    # Load weather data for the selected dates
    for date in selected_dates:
        weather_data_for_selected_date = load_weather_data(date)
        if weather_data_for_selected_date is not None:
            output += f" 8월 {date}일 날씨 \n" 
            output += weather_data_for_selected_date.to_string(index=False, col_space=25, justify='left')  
        output += "\n" + "-" * 95 + "\n"
    
    return output



#===============================


# import time
# from selenium import webdrivers
# from selenium.webdriver.common.by import By
# import pandas as pd
# from bs4 import BeautifulSoup
# import sys

# #keyword = sys.argv[1]
# keyword="서귀포"
# url = f"https://www.mangoplate.com/search/{keyword}"



# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--headless")  
# driver = webdriver.Chrome(options = chrome_options) # GUI 없이 런 
# #driver = webdriver.Chrome()
# driver.get(url)

# req = driver.page_source
# soup = BeautifulSoup(req, "html.parser")
# info_list = soup.find_all(name="div", attrs={"class":"info"})

# # 페이지 주소 저장
# page_urls = []
# page_url_base = "https://www.mangoplate.com"

# for info in info_list:
#     review_url = info.find(name="a")
#     if review_url is not None:
#         page_urls.append(page_url_base + review_url.get("href"))

# # 5개 url 크롤링
# titles = []
# total_scores = []
# addresses = []
# menus = []

# for url in page_urls[0:5]:
#     driver.get(url)

#     element = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > header > div.restaurant_title_wrap > span > h1'
#     title_raw = driver.find_element(By.CSS_SELECTOR, element)
#     title = title_raw.text
#     titles.append(title)

#     element = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > header > div.restaurant_title_wrap > span > strong > span'
#     total_raw = driver.find_element(By.CSS_SELECTOR, element)
#     total_score = total_raw.text
#     total_scores.append(total_score)

#     element = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(1) > td > span.Restaurant__InfoAddress--Text'
#     total_raw = driver.find_element(By.CSS_SELECTOR, element)
#     address = total_raw.text
#     addresses.append(address)

#     # 대표 메뉴
#     from selenium.common.exceptions import NoSuchElementException

#     element1 = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(2) > td > span'
#     element2 = 'body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(3) > td > span'

#     try:
#         total_raw = driver.find_element(By.CSS_SELECTOR, element1)
#     except NoSuchElementException:
#         try:
#             total_raw = driver.find_element(By.CSS_SELECTOR, element2)
#         except NoSuchElementException:
#             total_raw = None

#     if total_raw:
#         menu = total_raw.text
#         menus.append(menu)

# driver.quit()

# # 데이터 프레임으로 변환
# data = {
#     '< Title >': titles,
#     '< Score >': total_scores,
#     '< Address >': addresses,
#     '< Menu >': menus
# }
# df = pd.DataFrame(data)

# # csv로 저장
# file_name = 'mango_data.csv'
# df.to_csv(file_name,index=False, encoding = 'utf-8-sig')

# # 표를 깔끔하게 출력
# from tabulate import tabulate

# print()
# print('*' * 184)
# print("\n< 맛집 정보 >")
# print(tabulate(df, headers='keys', tablefmt='plain', showindex=False, numalign='center'))