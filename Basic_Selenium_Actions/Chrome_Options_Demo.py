from selenium import webdriver

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("--start-maximized")
chrome_Options.add_argument("headless")
chrome_Options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver',options=chrome_Options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
driver.quit()