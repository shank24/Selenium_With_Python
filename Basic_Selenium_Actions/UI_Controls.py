
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver')
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
#Checkbox Code
checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")

print("No. of Checkboxes",len(checkbox))

for chBox in checkbox:
    print(chBox.get_attribute("value"))
    if chBox.text == 'option2':
        chBox.click()
        assert chBox.is_selected()


#RadioButton Code
radioButton = driver.find_elements_by_name("radioButton")
radioButton[2].click()
assert radioButton[2].is_selected()


driver.find_element_by_id('hide-textbox').click()
assert not driver.find_element_by_id('displayed-text').is_displayed()
driver.close()