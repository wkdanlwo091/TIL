import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
# webbrowser.open('www.google.co.kr')
# # webbrowser.open_new('www.naver.com')
# webbrowser.open_new_tab('www.daum.net')

# res = requests.get('http://naver.com')

# print(res)
# print(res.text)
# print(res.status_code)


# soup = BeautifulSoup(response, 'html.parser')

# url = 'https://finance.naver.com/sise/' ## url 복사했던 정보--> 파싱할 웹의 주소 
# response = requests.get(url).text
# soup = BeautifulSoup(response, 'html.parser')
# kospi = soup.select_one('#KOSPI_now')
# print(kospi.text)


# url2 = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
# response = requests.get(url2).text
# soup = BeautifulSoup(response, 'html.parser')
# exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
# print(exchange.text)

url2 = 'https://www.naver.com/'
response = requests.get(url2).text
soup = BeautifulSoup(response, 'html.parser')
now = datetime.now()
search_ranking = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li .ah_k')
print(f'{now}')
print(search_ranking)#20개의 데이터

for name in search_ranking:
    print(name.text)


print("순위")

for i, name in enumerate(search_ranking):
    print(f'{i+1}위: {name.text}')
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li .ah_k  ### 1위부터 여러개 뽑기 위해서 중복되는 것들을 지움 

# or 
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k

#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(2) > a > span.ah_k



