
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_application():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-features=HttpsUpgrades")

    driver = webdriver.Remote(
        command_executor="http://chrome:4444/wd/hub",
        options=options
    )

    try:
        driver.get("http://172.18.0.3:8000/")

        print("Current URL:", driver.current_url)
        print("Page Title:", driver.title)

        assert driver.title == "CI/CD Testing Application"

        heading = driver.find_element(By.TAG_NAME, "h1")

        assert heading.text == "Welcome to CI/CD Pipeline Testing"

        print("Selenium test passed successfully!")

    finally:
        driver.quit()
