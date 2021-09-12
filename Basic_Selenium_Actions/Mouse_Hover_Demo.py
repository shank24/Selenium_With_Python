from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
action = ActionChains(driver)
menu = driver.find_element_by_id('mousehover')
action.move_to_element(menu).perform()
reloadMenu = driver.find_element_by_link_text("Reload")
action.move_to_element(childMenu).click().perform()
driver.quit()

