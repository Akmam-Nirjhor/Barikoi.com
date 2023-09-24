import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome("chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="geckodriver.exe")
    else:
        raise ValueError("Invalid browser name provided.")

    driver.get("https://dev-akmamnirjhor10.pantheonsite.io/wp-login.php?redirect_to=https%3A%2F%2Fdev-akmamnirjhor10.pantheonsite.io%2Fwp-admin%2Fadmin.php%3Fpage%3Dwp-dark-mode-settings&reauth=1 ")
    driver.maximize_window()

    request.cls.driver = driver
    yield driver

