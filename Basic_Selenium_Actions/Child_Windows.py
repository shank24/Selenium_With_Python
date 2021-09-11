from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://the-internet.herokuapp.com/windows")

driver.maximize_window()

driver.find_element_by_xpath(".//a[text()='Click Here']").click()
#Switching to Child Window
getWindows = driver.window_handles
driver.switch_to.window(getWindows[1])
assert "New Window" == driver.find_element_by_tag_name("h3").text
driver.close()
#Switching to Parent Window
#driver.close(getWindows[1])
driver.switch_to_window(getWindows[0])
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
driver.close()