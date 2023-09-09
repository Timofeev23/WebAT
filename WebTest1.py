from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#service = Service(executable_path='C:\Users\Admin\WebAT\chromedriver')  # указываем путь до драйвера
browser = webdriver.Chrome()

url = "https://ya.ru"

try:
    browser.get(url=url)
    
except:

finally:
    browser.close()
    browser.quit()


