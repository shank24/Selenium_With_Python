import pytest
from Selenium_Framework.pageObjects.HomePage import HomePage
from Selenium_Framework.testData.HomePageData import HomePageData
from Selenium_Framework.utilities.BaseClass import BaseClass as BC


class TestHomePage(BC):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        log.info("On HomePage")
        homePage = HomePage(self.driver)
        log.info("Sending FirstName & Email")
        homePage.getName().send_keys(getData["FirstName"])
        homePage.getEmail().send_keys(getData["Email"])
        homePage.getCheckBox().click()
        self.selectOptionByText(homePage.getGender(), getData["Gender"])

        log.info("Hitting Submit")
        homePage.submitForm().click()
        message = homePage.getMessage().text

        log.info("Asserting Success Message")
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Test2"))
    def getData(self, request):
        return request.param
