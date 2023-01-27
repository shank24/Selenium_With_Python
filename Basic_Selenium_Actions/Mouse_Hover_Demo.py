from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
action = ActionChains(driver)

menu = driver.find_element_by_id('mousehover')
action.move_to_element(menu).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
driver.quit()

