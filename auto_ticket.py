from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time 

from bs4 import BeautifulSoup

url = 'https://tixcraft.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)



while True:
    try:
        item = driver.find_element_by_id('activity')
        break
    except:
        continue

while True:
    try:
        item.click()
        break
    except:
        continue


while True:
    try:
        content = driver.find_elements_by_css_selector('a.fcDark')
        for d in content:
            if "老男孩" in d.text:
                d.click()
                break
        break
    except:
        continue

while True:
    try:
        print('here')
        item = driver.find_elements_by_css_selector('a.btn')
        break
    except Exception as e:
        print(e)
        continue

while True:
    try:
        print('AAA')
        for btn in item:
            if "立即購票" in btn.text:
                btn.click()
                break
        break
    except Exception as e:
        print(e)
        continue
        


while True:
    try:
        print('BBB')
        item = driver.find_element_by_name('yt0')
        break
    except Exception as e:
        print(e)
        continue

while True:
    try:
        item.click()
        break
    except:
        continue

while True:
    try:
        item = driver.find_element_by_class_name('closeNotice')
        break
    except:
        continue

while True:
    try:
        item.click()
        break
    except:
        continue

while True:
    try:
        items = driver.find_elements_by_tag_name('a')
        for item in items:
            if '特1區' in item.text:
                item.click()
                break
        break
    except:
        continue



while True:
    try:
        select = Select(driver.find_element_by_id('TicketForm_ticketPrice_01'))
        break
    except Exception as e:
        continue

while True:
    try:
        select.select_by_visible_text("3")
    except Exception as e:
        continue