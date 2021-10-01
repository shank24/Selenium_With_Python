from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitles)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)