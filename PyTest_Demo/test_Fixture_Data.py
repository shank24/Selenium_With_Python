import pytest
#from PyTestDemo.BaseClass import BaseClass as BC
import BaseClass as BC


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BC):

    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info("Testing editProfile")
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        log.info(dataLoad[2])
        print(type(dataLoad))
        #print(dataLoad)
