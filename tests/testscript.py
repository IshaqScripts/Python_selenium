from telnetlib import EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.wait import WebDriverWait

from webdriver_factory import WebDriverFactory
import time

if __name__ == "__main__":
    browser_name = "chrome" # Change this to the browser you want to use
    driver = WebDriverFactory.get_webdriver(browser_name)

    try:
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.find_element("XPATH", "//input[@value='radio2']").click()
        dropdown = driver.find_element("XPATH", "//input[@id='autocomplete']")
        dropdown.click()

        # Type "India" into the dropdown's input field
        input_field = driver.find_element("XPATH", "//input[@placeholder='Type to Select Countries']").send_keys("India")
        # Wait for the dropdown options to load and find the option for "India"
        try:
            india_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(("XPATH", "//ul[contains(@class, 'ui-menu')]//div[contains(text(), 'India')]")))
            india_option.click()
            print("India was found and selected.")
        except:
            print("India was not found in the dropdown options.")

        time.sleep(10)
    finally:
        driver.quit()
