from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url="https://ivorypaint.netlify.app/"
driver.get(url)

time.sleep(5)#wait for React to load

        
print(driver.page_source)

with open("index.html","w", encoding="utf-8") as f:
    f.write(driver.page_source)
    
