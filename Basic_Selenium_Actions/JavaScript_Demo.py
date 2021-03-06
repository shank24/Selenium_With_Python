#JS Dom can access any element on web page just like how selenium does
# Selenium have a method to execute Javascript code in it.


from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element_by_name('name').send_keys("Cherry")

#print(driver.find_element_by_name('name').text)
sel = driver.find_element_by_name('name').get_attribute('value')
jsConsole = driver.execute_script('return document.getElementsByName("name")[0].value')
assert sel == jsConsole

shopBtn = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();" , shopBtn)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.close()