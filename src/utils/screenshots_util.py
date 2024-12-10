import os
import time


def capture_screenshot(driver, name):
    """
    Captures a screenshot of the current state of the browser and saves it in the 'screenshots' directory.

    Args:
        driver (webdriver): Selenium WebDriver instance controlling the browser.
        name (str): Descriptive name for the screenshot file (e.g., test case or scenario name).

    Side Effects:
        Creates the 'screenshots' directory if it doesn't exist.
        Saves the screenshot in the directory with a timestamp in its filename.

    Example:
        capture_screenshot(driver, 'test_case_1')
    """
    # Get the relative path to the 'screenshots' folder from the current directory
    screenshots_directory = os.path.join(os.path.dirname(__file__), '..', 'execution_results', 'screenshots')

    # Create the screenshots folder if it does not exist
    if not os.path.exists(screenshots_directory):
        os.makedirs(screenshots_directory)

    # Generate the filename with the scenario name and current timestamp
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"execution_results/screenshots/{name}_{timestamp}.png"

    time.sleep(1)  # This wait is important to stabilize the screenshot
    driver.save_screenshot(screenshot_filename)
    time.sleep(1)  # This wait is important to stabilize the screenshot
