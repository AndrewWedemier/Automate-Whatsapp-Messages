from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


contact = "###"
text = "Hey, this message was sent using Selenium"
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
#input()
print("Logged In")

inp_xpath_search = '//div[@title="New chat"]'
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))

time.sleep(5)
input_box_search.click()
time.sleep(2)
input_xpath_1 = '//div[@contenteditable="true"][@data-tab="3"][@dir="ltr"]'
keyable_area=input_box_search.find_element_by_xpath(input_xpath_1)
#time.sleep(1)
keyable_area.send_keys(contact) 
time.sleep(4)
keyable_area.send_keys(Keys.ENTER)
time.sleep(2)
input_xpath_2 = '//div[@contenteditable="true"][@data-tab="1"]'
input_box=driver.find_element_by_xpath(input_xpath_2)
print(input_box)
text = "😘" 
input_box.click();

hours_in_day = 24
minutes_in_day = 24*60
five_minutes_in_day = minutes_in_day // 5

for i in range(five_minutes_in_day):
    input_box.send_keys(text)
    input_box.send_keys(Keys.ENTER)
    time.sleep(60*5)
