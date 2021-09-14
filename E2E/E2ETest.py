from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("--start-maximized")
#chrome_Options.add_argument("headless")
chrome_Options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver',options=chrome_Options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()

#Gettign the parent element locator
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

#Traversing through based on Condition

for prod in products:
    prodName = prod.find_element_by_xpath('div/h4/a').text
    if prodName == "Blackberry":
        prod.find_element_by_xpath('div/button').click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_css_selector("button[class*='btn-success']").click()
driver.find_element_by_id('country').send_keys('ind')

#Explicit Wait
wait = WebDriverWait(driver , 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
successText  = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in successText

driver.get_screenshot_as_file("screen.png")
driver.close()

