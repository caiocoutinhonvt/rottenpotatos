from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import ipdb; ipdb.set_trace()
chrome_options = Options()
PATH = "/home/pc/Desktop/DJANGO FULL PROJECT/chromedriver"
service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://letterboxd.com/films/popular/")
titles = driver.find_element(By.CLASS_NAME, 'poster-list')
poster = titles.find_elements(By.CLASS_NAME, 'listitem')


for posters in poster[:10]:
    title = posters.find_element(By.TAG_NAME, 'a').text
    print(title)
