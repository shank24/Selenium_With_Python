import pytest
from selenium import webdriver


driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setUp(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    #Chrome Invoke
    if browser_name == "chrome":
        chrome_Options = webdriver.ChromeOptions()
        #chrome_Options.add_argument("--start-maximized")
        # chrome_Options.add_argument("headless")
        chrome_Options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(executable_path='/home/shanky/PycharmProjects/chromedriver', options=chrome_Options)
    #Firefox Invoke
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path='/home/shanky/PycharmProjects/geckodriver')

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
