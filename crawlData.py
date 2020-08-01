from selenium import webdriver
from bs4 import BeautifulSoup
import time
#from webdriver_manager.chrome import ChromeDriverManager

def get_html_source_by_selenium(url):
    driver_chrome = webdriver.Chrome('C:/Users/HP/Desktop/chromedriver_win32/chromedriver.exe')
    driver_chrome.get(url)
    time.sleep(1)
    return driver_chrome.page_source

page = get_html_source_by_selenium('https://iboard.ssi.com.vn/bang-gia/vn30')
soup = BeautifulSoup(page, 'html.parser')
value_areas = soup.find_all('tbody', {'id' :'table-body-scroll'})
value_parts = value_areas[0].findChildren('tr')
c = value_parts[0].findChildren('td', recursive=False)
for i in c:
	print(i.text)
	print('\n')