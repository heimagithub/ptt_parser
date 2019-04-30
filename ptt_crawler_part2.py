import requests
from bs4 import BeautifulSoup
import re
import time

url = 'https://www.ptt.cc/bbs/Insurance/index1921.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
title = soup.find_all("div", class_="title")

# print(len(title))
# return 

data = []
for t in title:
    print(t)
    try:
        data.append({"sub_url": t.a['href'],
                     "title": t.text})
    except:
        pass

keywords = {'career':'職業',
            'budget':'預算',
            'demand': '需求',
            'sex': '性別',
            'age': '年齡'}

for d in data:
    url = "https://www.ptt.cc"+d['sub_url']
    
#     print(url)
#     break

    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "lxml")
    content = soup.find_all("meta")
    
    result = {}
    lines = str(content).split('\n')
    for line in lines:
        for key, val in keywords.items():
            if val in line:
                try:
                    if key == 'age':
                        tmp = re.sub("[^0-9]", '', line.split('：')[1])
                        result[key] = tmp
                    else:
                        result[key] = line.split('：')[1]
                except:
                    pass
                
#     print(result)
    time.sleep(3)
