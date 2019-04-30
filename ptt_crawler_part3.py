import requests
from bs4 import BeautifulSoup
import re 
import time
import pymysql

CONN = pymysql.connect(host='localhost',
                       user='root',
                       password='0',
                       cursorclass=pymysql.cursors.DictCursor)
cur = CONN.cursor()

keywords = {'career':'職業',
			'budget':'預算',
			'demand': '需求',
			'sex': '性別',
			'age': '年齡'}

def qeury_keywords(data):

	result = {}
	lines = data.split('\n')
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

	return result

def parse_content(sub_url):
	url = "https://www.ptt.cc"+sub_url
	response = requests.get(url)

	soup = BeautifulSoup(response.text, "lxml")
	content = soup.find_all("meta")

	result = qeury_keywords(str(content))

	return result

def parse_title(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "lxml")
	title = soup.find_all("div", class_="title")

	data = []
	for t in title:
		try:
			data.append({"sub_url": t.a['href'],
						 "title": t.text})
		except:
			pass

	next_page = soup.find("a", string="‹ 上頁")

	return data, next_page['href']

def main():

	base_url = 'https://www.ptt.cc'
	url = base_url+'/bbs/Insurance/index.html'

	while True:

		titles, next_page = parse_title(url)
		url = base_url+next_page 

		for title in titles:
			if "險種" in title['title']:
				data = parse_content(title['sub_url'])
				if len(data.keys()) < 3:
					continue

				data['url'] = base_url+title['sub_url']

				sql = 'INSERT INTO `insurance`.`ptt` (`sex`, `age`, `career`, `budget`, `demand`, `url`) VALUES (%s, %s, %s, %s, %s, %s);'
					
				try:
					cur.execute(sql, (data.get('sex'),
									  data.get('age'),
									  data.get('career'),
									  data.get('budget'),
									  data.get('demand'),
									  data.get('url')))
				except Exception as e:
					print(data)
					print(e)
				
				CONN.commit()
				time.sleep(3)


if __name__ == '__main__':
	main()