from selenium.webdriver.common.by import By

from Selenium_Framework.pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    successBtn = (By.CSS_SELECTOR,"button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitles)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutBtn)

    def getSuccessButton(self):
        self.driver.find_element(*CheckOutPage.successBtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage