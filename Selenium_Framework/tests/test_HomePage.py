from selenium import webdriver
from selenium.webdriver.support.select import Select

from Selenium_Framework.pageObjects.HomePage import HomePage
from Selenium_Framework.utilities.BaseClass import BaseClass as BC


class TestHomePage(BC):

    def test_formSubmission(self):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys("Shank")
        homePage.getEmail().send_keys("Karan@gmail.com")
        homePage.getCheckBox().click()

        # Select Class Demo
        dropdown = Select(homePage.getGender())
        dropdown.select_by_visible_text("Female")
        dropdown.select_by_index(0)

        homePage.submitForm().click()
        message = homePage.getMessage().text

        assert "Success" in message

