from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector('#name').send_keys('Option3')
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to_alert()
print(alert.text)
alert.accept()

driver.close()