import time

from selenium import webdriver



driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")

#driver.find_element_by_css_selector('input.search-keyword').send_keys("ber")
time.sleep(4)
length = len(driver.find_elements_by_xpath(".//div[@class='products loading']/div"))

print(length)

driver.close()