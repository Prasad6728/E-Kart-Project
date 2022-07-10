import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("D:/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


driver.find_element("css selector", ".search-keyword").send_keys("ber")
time.sleep(4)
lists = driver.find_elements("xpath", value=("//div[@class='products']/div"))
count = len(lists)

assert count == 3

buttons = driver.find_elements("css selector", value=("div[class='product-action'] button"))
for i in buttons:
    i.click()
    time.sleep(4)

driver.find_element("css selector", value=("img[alt='Cart']")).click()
driver.find_element("xpath", value=("//button[text()='PROCEED TO CHECKOUT']")).click()  # Using text() in Xpath == no @
time.sleep(4)
driver.find_element("css selector", value=('.promoCode')).send_keys("rahulshettyacademy")
driver.find_element("css selector", value=(".promoBtn")).click()
time.sleep(7)
print(driver.find_element("css selector" , value=('span.promoInfo')).text)





