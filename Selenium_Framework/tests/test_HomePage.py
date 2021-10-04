import pytest
from Selenium_Framework.pageObjects.HomePage import HomePage
from Selenium_Framework.utilities.BaseClass import BaseClass as BC


class TestHomePage(BC):

    def test_formSubmission(self,getData):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["FirstName"])
        homePage.getEmail().send_keys(getData["Email"])
        homePage.getCheckBox().click()
        self.selectOptionByText(homePage.getGender(), getData["Gender"])

        homePage.submitForm().click()
        message = homePage.getMessage().text

        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=[{"FirstName" : "Shank", "Email" : "Karan@gmail.com", "Gender" : "Male" }, {"FirstName" : "Cherry", "Email" : "Charneet@gmail.com", "Gender" : "Female" }])
    def getData(self, request):
        return request.param
