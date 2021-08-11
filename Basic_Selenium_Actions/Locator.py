from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://rahulshettyacademy.com/angularpractice/")
#Textbox
#driver.find_element_by_name("name").send_keys("Shank")
driver.find_element_by_css_selector("input[name='name']").send_keys("Shank")
#Checkbox
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath(".//input[@type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)

#Regular Expression
#print(driver.find_element_by_class_name([class*='alert-success']).text)
#//*[contains(@class,'alert-success')]

#Tag Name With css
#input#username
driver.close()