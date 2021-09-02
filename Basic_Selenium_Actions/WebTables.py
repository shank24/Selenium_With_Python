
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")

driver.maximize_window()
value = driver.find_elements_by_xpath("//tr/td[5]")

sum = 0
for val in value:
    sum = sum + int(val.text)

print(sum)
driver.close()