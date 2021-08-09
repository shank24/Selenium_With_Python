from selenium import webdriver
#Browser exposes an exe file
#Through Selenium test, we need to invoke the executable file
#which will invoke actual browser
driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
#driver = webdriver.Firefox(executable_path='/home/shanky/PycharmProjects/geckodriver')
driver.get("https://www.hackerrank.com/")
driver.maximize_window()
print(driver.title)
driver.minimize_window()
driver.get("https://www.hackerrank.com/skills-verification")
print(driver.title)
driver.back()
driver.refresh()
driver.close()
