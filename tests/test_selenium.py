from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_google_search(setup):
    driver = setup
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.NAME, "username").send_keys("student")
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    assert "Logged In Successfully" in driver.title
