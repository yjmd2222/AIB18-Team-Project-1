#셀레니움 실행

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

keyword = "혜화역"
url=f"https://www.mangoplate.com/search/{keyword}"

driver = webdriver.Chrome() 
driver.get(url)

time.sleep(2)

# find all the elements with the store titles
store_titles_elements = driver.find_elements(By.CSS_SELECTOR, '.title')

# extract the titles and store them in a list
store_titles = [element.text for element in store_titles_elements]

# cut the titles after the 10st index
store_titles = store_titles[:11]

# create a dataframe from the list of store titles
df = pd.DataFrame({'Store Titles': store_titles})

# print the dataframe
print(df)

# close the browser
driver.quit()