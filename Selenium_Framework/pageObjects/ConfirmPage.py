from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryLink = (By.ID, "country")

    def searchCountry(self,countryName):
        return self.driver.find_element(*ConfirmPage.countryLink).send_keys(countryName)
