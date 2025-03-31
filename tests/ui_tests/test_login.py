from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def test_login():
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://the-internet.herokuapp.com/login")

    # Fill in the login form
    driver.find_element(By.NAME, "username").send_keys("tomsmith")
    driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Assert that the login was successful
    success_message = driver.find_element(By.CSS_SELECTOR, "#flash").text
    assert "You logged into a secure area!" in success_message

    driver.quit()

test_login()
