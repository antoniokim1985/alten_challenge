from behave import given, when, then
from selenium import webdriver
from pages.AltenPage import AltenPage
from pages.UnetePage import UnetePage
from utils.logging_util import logging

logging.basicConfig(level=logging.INFO)
driver = webdriver.Chrome()

# Initialize page objects once
alten_page = AltenPage(driver)
unete_page = UnetePage(driver)

def ensure_cookies_checked(page):
    """
    Ensures cookies are checked and handled for a given page.

    Args:
        page (object): Page object to check cookies on (e.g., AltenPage or UnetePage).
    """
    page.check_cookies()

@given('I open the Alten homepage')
def open_alten_homepage(context):
    driver.get("https://www.alten.es")
    ensure_cookies_checked(alten_page)

@when('I search for "{term}" in the header')
def search_for_query(context, term):
    ensure_cookies_checked(alten_page) # This process has been repeated as the pop-up has appeared despite being previously accepted.
    alten_page.perform_search(term)

@then('I should see "{results}" search results for "{term}" in the header')
def check_search_results(context, term, results):
    ensure_cookies_checked(alten_page) # This process has been repeated as the pop-up has appeared despite being previously accepted.
    alten_page.result_counts(term, results)

@when('I go to Unete a nosotros')
def go_to_unete(context):
    ensure_cookies_checked(alten_page) # This process has been repeated as the pop-up has appeared despite being previously accepted.
    alten_page.go_to_unete()

@when('I go to Nuestras ofertas de empleo')
def go_to_nuestras_ofertas(context):
    unete_page.go_to_nuestras_ofertas()

@when('I seek by "{term}" in ofertas de empleo')
def search_in_ofertas(context, term):
    unete_page.seek_ofertas(term)

@then('I found only results with "{results}" in ofertas de empleo')
def result_in_ofertas(context, results):
    unete_page.result_in_ofertas(results)
