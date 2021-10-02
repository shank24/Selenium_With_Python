from selenium import webdriver
from selenium.webdriver.support.select import Select

from Selenium_Framework.pageObjects.HomePage import HomePage
from Selenium_Framework.utilities.BaseClass import BaseClass as BC


class TestHomePage(BC):

    def test_formSubmission(self):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys("Shank")
        #driver.find_element_by_css_selector("input[name='name']").send_keys("Shank")
        homePage.getEmail().send_keys("Karan@gmail.com")
        #driver.find_element_by_name("email").send_keys("Karan@gmail.com")
        homePage.getCheckBox().click()
        #driver.find_element_by_id("exampleCheck1").click()

        # Select Class Demo
        dropdown = Select(homePage.getGender())
        dropdown.select_by_visible_text("Female")
        dropdown.select_by_index(0)

        homePage.submitForm().click()
        #driver.find_element_by_xpath(".//input[@type='submit']").click()
        message = homePage.getMessage().text
        # message = driver.find_element_by_class_name("alert-success").text

        assert "Success" in message

