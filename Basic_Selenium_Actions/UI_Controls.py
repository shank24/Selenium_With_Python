import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkbox))

for chBox in checkbox:
    chBox.click()
    assert chBox.is_selected()

driver.close()