from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

driver.maximize_window()
action = ActionChains(driver)

doubleClickElement = driver.find_element_by_id('double-click')
action.double_click(doubleClickElement).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()

driver.quit()

