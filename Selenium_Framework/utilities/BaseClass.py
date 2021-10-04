import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setUp")
class BaseClass:

    def verifyLinkPresence(self, textToVerify):
        element = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.LINK_TEXT, textToVerify)))

    def selectOptionByText(self, locator, textToSelect):
        selectElem = Select(locator)
        selectElem.select_by_visible_text(textToSelect)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

            # file handler object is required in addHandler
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s :%(lineno)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
