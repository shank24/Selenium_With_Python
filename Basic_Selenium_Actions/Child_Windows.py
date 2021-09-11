from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://the-internet.herokuapp.com/windows")

driver.maximize_window()

driver.find_element_by_xpath(".//a[text()='Click Here']").click()
print(driver.find_element_by_tag_name("h3").text)
driver.close()