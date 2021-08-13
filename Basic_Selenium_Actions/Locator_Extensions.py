from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("Shank")
driver.find_element_by_css_selector(".password").send_keys("12345")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//input[@name='cancel']").click()
print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label[text()='Username']").text)
driver.close()



