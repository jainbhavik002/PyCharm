from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"
URL = "https://www.instagram.com/accounts/login/"

def login_bot(username, password, url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    wait = WebDriverWait(driver, 20)

    # Wait until username field is present
    user_input = wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    pass_input = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    user_input.send_keys(username)
    pass_input.send_keys(password)

    # Wait for and click login button
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()

    input("Logged in (or error shown). Press Enter to close...")
    driver.quit()

if __name__ == "__main__":
    login_bot(USERNAME, PASSWORD, URL)
