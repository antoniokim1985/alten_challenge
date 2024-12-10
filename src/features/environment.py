from utils.logging_util import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.report_util import generate_report

logging.basicConfig(level=logging.INFO)

def before_scenario(context, scenario):
    """
    Sets up the browser environment before the execution of a scenario.

    Args:
        context (obj): The context object to share data between steps.
        scenario (obj): The scenario object containing metadata about the scenario being executed.

    Side Effects:
        Initializes a Chrome WebDriver instance and assigns it to `context.driver`.

    Example:
        before_scenario(context, scenario)
    """
    logging.info(f"Starting scenario: {scenario.name}")
    options = Options()
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def after_scenario(context, scenario):
    """
    Cleans up the environment after the execution of a scenario.

    Args:
        context (obj): The context object to share data between steps.
        scenario (obj): The scenario object containing metadata about the scenario being executed.

    Side Effects:
        Generates a report based on the scenario's status.
        Logs the status of the scenario.
        Closes the WebDriver instance assigned to `context.driver`.

    Example:
        after_scenario(context, scenario)
    """
    if scenario.status == 'failed':
        logging.error(f"Test failed: {scenario.name}")
        generate_report(scenario.name, 'Failed', str(scenario.error_message))
    else:
        generate_report(scenario.name, 'Passed')
    context.driver.quit()
