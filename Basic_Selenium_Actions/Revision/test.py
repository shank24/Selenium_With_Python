from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service_ob=Service("/home/shanky/PycharmProjects/chromedriver")
driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')

#driver = webdriver.Chrome(service=service_ob)
driver.get("https://regexr.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url) 
driver.quit()