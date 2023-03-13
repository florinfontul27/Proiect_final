import selenium.webdriver
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def browser():
    #before tests
    global driver
    #initializam browserul
    s = Service(ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = selenium.webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    #return driver
    yield driver
    #after tests
    driver.quit()