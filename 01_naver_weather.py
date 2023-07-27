from bs4 import BeautifulSoup
import requests
import sys

#query = sys.argv[1] # flask확인 html용 

query = '신촌' # 개별 파일 디버깅용

# if len(query) > 1:
#     query = query
# else:
#     query = "제주도"

html = requests.get(f"https://search.naver.com/search.naver?where=nexearch&query={query}+날씨")
soup = BeautifulSoup(html.text, 'html.parser')

# 위치
address = soup.find('div', {'class': 'title_area _area_panel'}).find('h2', {'class' : 'title'}).text
print("")
print("위치: " + address)

# 날씨 정보
weather_data = soup.find('div', {'class': 'weather_info'})

# 현재 온도
tempertaure = weather_data.find('div', {'class': 'temperature_text'}).text.strip()[5:]
print("현재 온도: " +tempertaure)

# 날씨 상태
weather_status = weather_data.find('span', {'class': 'weather before_slash'}).text
print("날씨 상태: " +weather_status)


# 주간 날짜
week_weather_times = soup.find('div', {'class': 'list_box _weekly_weather'}).find('ul', {'class' : 'week_list'}).find_all('div', {'class' : 'cell_date'})

# 주간 최저/최고 기온
week_temperature_cells = soup.find('div', {'class': 'list_box _weekly_weather'}).find('ul', {'class':'week_list'}).find_all('div', {'class':'cell_temperature'})

# 주간 날씨 상태
#weather_icon = soup.find('div', {'class': 'list_box _weekly_weather'}).find('ul', {'class': 'week_list'}).find('div', {'class': 'cell_weather'}).find_all('span', {'class':'blind'})
week_weather_icons = soup.find('div', {'class': 'list_box _weekly_weather'}).find('ul', {'class': 'week_list'}).find_all('span', {'class':'blind'})



# 주간 합쳐서 프린트하기
print('')
print("< 주간 날씨 > ")
print('')
for a,b,c in zip(week_weather_times, week_temperature_cells,week_weather_icons):
    print(a.text+ '\t' +b.text+'\t' +c.text)


print()
print('*' * 180) # 가름선
print("\n< 오늘 시간대 별 날씨 정보 >")
weather_time = soup.find_all('li', {'class': '_li'}) #  시간 li를 다 가져옴 

weather_list = []


for i in weather_time[:24]:# 현시간부터 24시간
    # print(i.text.strip()) # 기존 출력 형태
    weather_list.append(i.text.strip())

### 출력 포맷 변경
times = []
weathers = []
temperatures = []

for item in weather_list:
    time, weather_temp = item.split(maxsplit=1)
    if time == '내일':
        time = '24시'
    weather, temp = weather_temp.split() # 붙어있는 거 자르기
    times.append(time)
    weathers.append(weather)
    temperatures.append(temp)

# Format the output
column_width = 8

times_part1, times_part2 = times[:12], times[12:] # 가독성을 위해 24개를 2줄로 나누어 줌 
weathers_part1, weathers_part2 = weathers[:12], weathers[12:]
temperatures_part1, temperatures_part2 = temperatures[:12], temperatures[12:]

formatted_times_part1 = '\t'.join(time.ljust(column_width) for time in times_part1)
formatted_weathers_part1 = '\t'.join(weather.lower().ljust(column_width) for weather in weathers_part1)
formatted_temperatures_part1 = '\t'.join(temperature.ljust(column_width) for temperature in temperatures_part1)

formatted_times_part2 = '\t'.join(time.ljust(column_width) for time in times_part2)
formatted_weathers_part2 = '\t'.join(weather.lower().ljust(column_width) for weather in weathers_part2)
formatted_temperatures_part2 = '\t'.join(temperature.ljust(column_width) for temperature in temperatures_part2)

formatted_output1 = f"{formatted_times_part1}\n{formatted_weathers_part1}\n{formatted_temperatures_part1}"
formatted_output2 = f"{formatted_times_part2}\n{formatted_weathers_part2}\n{formatted_temperatures_part2}"

print(formatted_output1)
print()
print(formatted_output2)
