
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setUp")
class BaseClass:

    def verifyLinkPresence(self, textToVerify):
        element = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.LINK_TEXT, textToVerify)))

    def selectOptionByText(self,locator, textToSelect):
        selectElem = Select(locator)
        selectElem.select_by_visible_text(textToSelect)