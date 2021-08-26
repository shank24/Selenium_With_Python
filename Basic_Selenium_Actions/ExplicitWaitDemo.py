from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

#homeBtn = driver.find_element_by_xpath(".//button[@class='btn btn-primary' and text()='Home']")
wait = WebDriverWait(driver , 5)
wait.until(EC.presence_of_element_located((By.XPATH,".//button[@class='btn btn-primary' and text()='Home']")))
wait.until(EC.presence_of_element_located((By.CLASS_NAME,"btn.btn-primary")))

driver.close()