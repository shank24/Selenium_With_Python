import pytest
from Selenium_Framework.pageObjects.HomePage import HomePage
from Selenium_Framework.utilities.BaseClass import BaseClass as BC


class TestHomePage(BC):

    def test_formSubmission(self,getData):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData[0])
        homePage.getEmail().send_keys(getData[1])
        homePage.getCheckBox().click()
        self.selectOptionByText(homePage.getGender(), getData[2])

        homePage.submitForm().click()
        message = homePage.getMessage().text

        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=[("Shank", "Karan@gmail.com", "Male"), ("Charneet", "Charneet@gmail.com", "Female")])
    def getData(self, request):
        return request.param
