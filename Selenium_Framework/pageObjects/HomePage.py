from selenium.webdriver.common.by import By


class HomePage:

    shop = (By.CSS_SELECTOR,"a[href*='shop']")

    def shopItems(self):
        driver.find_element(*HomePage.shop)