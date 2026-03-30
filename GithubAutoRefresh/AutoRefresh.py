from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():

    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://github.com/aniketkumarpathak/PythonWithSelenium")

        # Wait until page loads
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        for i in range(5):
            driver.refresh()
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print(f"Refreshed {i+1} times")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
