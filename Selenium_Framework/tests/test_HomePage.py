import pytest
from Selenium_Framework.pageObjects.HomePage import HomePage
from Selenium_Framework.testData.HomePageData import HomePageData
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

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
