from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")
name = driver.find_element_by_name("name")
name.send_keys("Shank")
driver.close()