import requests
from bs4 import BeautifulSoup
import re
import time

# requests 爬取網頁資料
url = 'https://www.ptt.cc/bbs/Insurance/M.1556121185.A.023.html'
response = requests.get(url)
print(response.text)

# BeautifulSoup 方便檢索
soup = BeautifulSoup(response.text, "lxml")
text = soup.find_all("meta")
print(text[4])

# 爬取 關鍵字資料
sex = re.search('(?<=性別：)\w+', str(text[4]))
print(sex.group(0))

age = re.search('(?<=年齡：)\w+', str(text[4]))
print(age.group(0))

career = re.search('(?<=職業/工作內容：)\w+', str(text[4]))
print(career.group(0))