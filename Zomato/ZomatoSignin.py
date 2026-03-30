from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import sys

def main():

    driver = webdriver.Chrome()   # No hardcoded path
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.zomato.com/ncr")

        # Sign in button (By.ID)
        signin_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "signin-link"))
        )
        signin_btn.click()

        # Login via email (By.ID)
        login_email = wait.until(
            EC.element_to_be_clickable((By.ID, "login-email"))
        )
        login_email.click()

        # Enter email (By.NAME)
        email_field = wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys("noreplymuthukumar@gmail.com")

        # Submit button (By.CSS_SELECTOR)
        submit_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input#ld-submit-global"))
        )
        submit_btn.click()

        # OTP Input (By.CLASS_NAME)
        print("Enter OTP: ")
        otp = sys.stdin.readline().strip()

        otp_field = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "verification-code-value"))
        )
        otp_field.send_keys(otp)

        # Click Continue (By.XPATH)
        continue_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='ld-login-otp-page']/div[2]/a"))
        )
        continue_btn.click()

        print("Login Successful")

    except TimeoutException:
        print("Element not found within time limit")

    except NoSuchElementException:
        print("Element does not exist")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
