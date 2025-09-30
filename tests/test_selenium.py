# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import pytest
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# @pytest.fixture
# def setup():
#     # Configure Chrome for headless mode (for CI)
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run without GUI
#     chrome_options.add_argument("--no-sandbox")  # Needed for CI
#     chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid resource issues
#     chrome_options.add_argument("--window-size=1920,1080")  # Set window size

#     # Use WebDriver Manager to install ChromeDriver
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=chrome_options
#     )
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# def test_google_search(setup):
#     driver = setup
#     driver.get("https://practicetestautomation.com/practice-test-login/")

#     # Use explicit waits instead of time.sleep
#     wait = WebDriverWait(driver, 10)

#     username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#     username_input.send_keys("student")

#     password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
#     password_input.send_keys("Password123")

#     submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
#     submit_button.click()

#     # Wait for page title or a success message element
#     wait.until(EC.title_contains("Logged In Successfully"))

#     assert "Logged In Successfully" in driver.title

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    # Configure Chrome options for headless mode (CI-friendly)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without GUI
    chrome_options.add_argument("--no-sandbox")  # Required for CI
    chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid resource issues
    chrome_options.add_argument("--window-size=1920,1080")  # Optional: set window size

    # Automatically download and use the correct ChromeDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    yield driver
    driver.quit()

def test_google_login(setup):
    driver = setup
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Use explicit waits instead of time.sleep
    wait = WebDriverWait(driver, 10)

    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_input.send_keys("student")

    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys("Password123")

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    submit_button.click()

    # Wait for page title or success message
    wait.until(EC.title_contains("Logged In Successfully"))

    # Assertion
    assert "Logged In Successfully" in driver.title
