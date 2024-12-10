from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tools.Tools import Tool
from utils.screenshots_util import capture_screenshot
from utils.logging_util import logging
import time

class UnetePage:
    def __init__(self, driver):
        self.driver = driver
        self.tool = Tool(driver)
        self.nuestras_ofertas = '/html/body/div[1]/div/div/div[1]/div[3]/div/a'
        self.input_ofertas = '/html/body/div[1]/div/div/div[2]/div/form/div/div[2]/div[1]/div/div/input'
        self.list_result_ofertas = '/html/body/div[1]/div/div/div[2]/div/form/div/div[2]/div[6]/div[1]/div[*]/div/a/b'

    def go_to_nuestras_ofertas(self):
        self.tool.wait_and_click(By.XPATH, self.nuestras_ofertas)

    def seek_ofertas(self, term):
        if self.tool.check_element_appearance(By.XPATH, self.input_ofertas):
            self.tool.wait_and_click(By.XPATH, self.input_ofertas)
            input_field = self.driver.find_element(By.XPATH, self.input_ofertas)
            input_field.clear()
            Tool.type_with_delay(input_field, term, 0.1)
            input_field.send_keys(Keys.RETURN)
            capture_screenshot(self.driver, f"Unete Page - Seeking {term}")


    def result_in_ofertas(self, results):
        if self.tool.check_element_appearance(By.XPATH, self.input_ofertas):
            found_results = self.driver.find_elements(By.XPATH, self.list_result_ofertas)
            for found_result in found_results:
                logging.info(found_result.text.lower())
                Tool.center_for_screenshot(self.driver, found_result)
                capture_screenshot(self.driver, f"Unete Page - Found {(found_result.text).replace('/', '_')} in {results}")
                assert results.lower() in found_result.text.lower()
