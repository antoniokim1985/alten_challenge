import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logging_util import logging

class Tool:
    """
    A utility class for interacting with web elements using Selenium WebDriver.

    Attributes:
        driver (WebDriver): The Selenium WebDriver instance used to control the browser.
    """

    def __init__(self, driver):
        """
        Initializes the Tool class with a WebDriver instance.

        Args:
            driver (WebDriver): Selenium WebDriver instance controlling the browser.
        """
        self.driver = driver

    def check_element_appearance(self, by, value, max_retries=10, interval=3):
        """
        Checks if an element appears on the page by performing periodic checks.

        Args:
            by (By): The method to locate the element (e.g., By.XPATH).
            value (str): The value used to locate the element (e.g., the XPath).
            max_retries (int, optional): Maximum number of attempts to check for the element. Defaults to 10.
            interval (int, optional): Waiting interval between attempts in seconds. Defaults to 3.

        Returns:
            bool: True if the element appears within the given retries, False otherwise.

        Example:
            tool.check_element_appearance(By.ID, "submit_button", max_retries=5, interval=2)
        """
        for attempt in range(max_retries):
            try:
                # Try to find the element
                element = WebDriverWait(self.driver, interval).until(
                    EC.visibility_of_element_located((by, value))
                )
                logging.debug(f"Element with {by}='{value}' found.")
                return True  # The element appeared, returning True
            except Exception as e:
                logging.debug(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(interval)  # Wait for the interval before trying again

        # If we reach this point, the element was not found after all attempts
        logging.error(f"Element with {by}='{value}' did not appear after {max_retries} attempts.")
        return False  # The element did not appear

    def wait_and_click(self, by, value, timeout=10):
        """
        Waits until the specified element is visible and clicks on it.

        Args:
            by (By): The method to locate the element (e.g., By.XPATH).
            value (str): The value used to locate the element (e.g., the XPath).
            timeout (int, optional): The maximum time to wait before an error occurs (in seconds). Defaults to 10.

        Example:
            tool.wait_and_click(By.CSS_SELECTOR, ".button-class", timeout=5)
        """
        try:
            # Wait until the element is visible
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            # Once visible, perform the click
            element.click()
            logging.debug(f"Element with {by}='{value}' found and clicked.")
        except Exception as e:
            logging.error(f"Error while attempting to click on the element: {e}")

    def center_for_screenshot(driver, xpath):
        """
        Scrolls the page to center the specified element for a screenshot.

        Args:
            driver: Web Driver
            xpath (WebElement): The web element to center in the viewport.

        Example:
            tool.center_for_screenshot(xpath)
        """
        try:
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});",
                xpath
            )
            logging.debug("Element centered in the viewport for screenshot.")
        except Exception as e:
            logging.error(f"Error while centering the element for screenshot: {e}")

    def type_with_delay(input_field, term, delay=0.1):
        """
        Types a given term into an input field with a delay between each keystroke.

        Args:
            input_field (WebElement): The input field element to type into.
            term (str): The text to type into the input field.
            delay (float, optional): The delay in seconds between each keystroke. Defaults to 0.1.

        Example:
            tool.type_with_delay(input_field, "example text", delay=0.2)
        """
        try:
            for letter in term:
                input_field.send_keys(letter)
                time.sleep(delay)
            logging.debug(f"Typed '{term}' into the input field with a delay of {delay} seconds between keystrokes.")
        except Exception as e:
            logging.error(f"Error while typing into the input field: {e}")
