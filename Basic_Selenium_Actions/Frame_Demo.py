from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://the-internet.herokuapp.com/iframe")

driver.maximize_window()

#iframe, frameset, frame
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Automate")
driver.switch_to_default_content()
print(driver.find_element_by_tag_name("h3").text)
driver.close()