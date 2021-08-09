from selenium import webdriver
#Browser exposes an exe file
#Through Selenium test, we need to invoke the executable file
#which will invoke actual browser
driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://www.hackerrank.com/")
driver.maximize_window()
driver.close()