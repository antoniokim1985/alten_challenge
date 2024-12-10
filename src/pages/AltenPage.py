from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tools.Tools import Tool
from utils.screenshots_util import capture_screenshot
from utils.logging_util import logging
import time

class AltenPage:
    def __init__(self, driver):
        self.driver = driver
        self.tool = Tool(driver)
        self.cookies_message = '/html/body/div[4]/div[4]/button[1]'
        self.search_button = '/html/body/div[1]/header/header[1]/div[1]/div[2]/div[1]/button/span'
        self.search_input = '/html/body/div[1]/header/header[1]/div[1]/div[2]/div[1]/form/div[1]/input'
        self.search_results_counter = '/html/body/div[1]/header/header[1]/div[1]/div[2]/div[1]/form/div[2]/div[1]/span[1]'
        self.menu_expandible = '/html/body/div[1]/header/header[1]/div[1]/div[2]/div[3]/div/div[1]'
        self.unete = '/html/body/div[1]/header/header[1]/div[2]/div[1]/div/ul/li[4]/a/span'
        self.nuestras_ofertas = '/html/body/div[1]/div/div/div[1]/div[3]/div/a'

    def check_cookies(self):
        if self.tool.check_element_appearance(By.XPATH, self.cookies_message, max_retries=3, interval=1):
            element = self.driver.find_element(By.XPATH, self.cookies_message)
            element.click()
            capture_screenshot(self.driver, "Alten HomePage - Cookies accepted")
            logging.info("Alten HomePage - Cookies accepted")
        else:
            pass

    def perform_search(self, term):
        self.tool.wait_and_click(By.XPATH, self.search_button)
        if self.tool.check_element_appearance(By.XPATH, self.search_input, max_retries=3, interval=1):
            input_field = self.driver.find_element(By.XPATH, self.search_input)
            input_field.clear()
            Tool.type_with_delay(input_field, term, 0.1)
            capture_screenshot(self.driver, f"Alten HomePage - Searching {term}")
            logging.info(f"Alten HomePage - Searching {term}")

    def result_counts(self, term, results):
        if self.tool.check_element_appearance(By.XPATH, self.search_results_counter):
            counter = self.driver.find_element(By.XPATH, self.search_results_counter)
            logging.info(f"Alten HomePage - {counter.text} results found searching by {term}")
            capture_screenshot(self.driver, f"Alten HomePage - Found {results} searching by {term}")
            assert counter.text == results

    def go_to_unete(self):
        self.tool.wait_and_click(By.XPATH, self.menu_expandible)
        self.tool.wait_and_click(By.XPATH, self.unete)
