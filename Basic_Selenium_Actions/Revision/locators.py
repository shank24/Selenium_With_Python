from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")

#nameElem = driver.find_element_by_name('name')
nameElem = driver.find_element(By.NAME, 'name')
nameElem.send_keys('Shanky')
driver.get_screenshot_as_file("screen.png")
driver.maximize_window()
driver.quit()