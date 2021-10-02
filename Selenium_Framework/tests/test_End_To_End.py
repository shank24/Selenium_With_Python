from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_Framework.pageObjects.HomePage import HomePage
from Selenium_Framework.utilities.BaseClass import BaseClass as BC


class TestOne(BC):

    def test_e2e(self):
        # Operations Of Home Page
        homepage = HomePage(self.driver)
        # Operations Of CheckOut Page
        checkOutPage = homepage.shopItems()

        # Getting the parent element locator
        products = checkOutPage.getCardTitles()
        # Traversing through based on Condition
        i = -1
        for prod in products:
            i = i + 1
            prodName = prod.text
            # prodName = prod.find_element_by_xpath('div/h4/a').text
            if prodName == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
                # prod.find_element_by_xpath('div/button').click()

        checkOutPage.getCheckoutButton().click()
        # Operations Of Confirm Page
        confirmPage = checkOutPage.getSuccessButton()
        confirmPage.searchCountry('ind')

        # Explicit Wait
        #element = WebDriverWait(self.driver, 7).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.verifyLinkPresence('India')
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")
        self.driver.close()
