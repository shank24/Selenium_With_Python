
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")

driver.maximize_window()
value = driver.find_elements_by_xpath("//tr/td[5]")
print(type(value))

sum = 0
for val in value:
    sum = sum + int(val.text)

print(sum)

# for i in range(1,6):
#     elements = driver.find_elements_by_xpath('//tr/td[1]')
#     print(elements.text)
#
driver.close()