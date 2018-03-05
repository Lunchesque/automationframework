import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, osType):

    baseUrl = "https://letskodeit.teachable.com"

    print("Running conftest demo oneTimeSetUp")
    if browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)
        print("Running test on FF")
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)
        print("Running test on Chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running conftest demo oneTimeTearDown")

@pytest.fixture()
def setUp():
    print("Running conftest demo setUp")
    yield
    print("Running conftest demo tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="type of OS")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
