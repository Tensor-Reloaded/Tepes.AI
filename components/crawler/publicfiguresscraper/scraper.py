import datetime
import os.path
import time

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from constants import *
from scraping_parser import get_parser
from CallDecorator import call_decorator


@call_decorator
def get_selenium_driver():
    DECLARATIONS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "declarations")
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': DECLARATIONS_PATH}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', prefs)
    return webdriver.Chrome(executable_path=LOCATIE_DRIVER, options=options)


@call_decorator
def search_declaratii_integritate(driver):
    buton_cauta_elem = driver.find_element("id", CAUTA_BUTON_ID)
    buton_cauta_elem.click()
    print("Performing new search!...")
    time.sleep(4)


@call_decorator
def descarca_declaratii_integritate(driver):
    try:
        element_present = EC.presence_of_element_located(("id", SEARCH_RESULT_ID))
        WebDriverWait(driver, 15).until(element_present)
    except TimeoutException:
        print("Timed out waiting for results to load")

    print("Searching for results!...")
    time.sleep(1)

    if driver.find_element("id", TOO_MANY_RECORDS).is_displayed():
        print("Too many records returned!...")
        time.sleep(4)
        driver.find_element("id", TOO_MANY_RECORDS_BUTTON).click()
    else:
        try:
            download_button = driver.find_element("id", DESCARCA_CSV)
            download_button.click()
            print("Downloading CSV!...")
            time.sleep(4)
        except NoSuchElementException:
            print("No records found!...")
            time.sleep(4)


@call_decorator
def scrape_declaratii_integritate(driver):
    open_advanced_search_page(driver)

    start_date = datetime.date(year=2020, month=11, day=1)
    end_date = datetime.date(year=2022, month=11, day=1)

    current_start_date = start_date
    while current_start_date <= end_date:
        current_end_date = current_start_date + datetime.timedelta(days=73)
        for localitate_index in range(3, 3167):
            try:
                element_present = EC.presence_of_element_located(("id", LOCALITATE_INPUT_ID))
                WebDriverWait(driver, 10).until(element_present)
            except TimeoutException:
                print("Timed out waiting for advanced search page to load")

            data_inceput_elem = driver.find_element("id", DATA_INCEPUT_INPUT_ID)
            data_inceput_elem.clear()
            data_inceput_elem.send_keys(current_start_date.strftime('%d.%m.%Y'))

            data_sfarsit_elem = driver.find_element("id", DATA_SFARSIT_INPUT_ID)
            data_sfarsit_elem.clear()
            data_sfarsit_elem.send_keys(current_end_date.strftime('%d.%m.%Y'))

            tip_declaratie_elem = driver.find_element("id", TIP_DECLARATIE_INPUT_ID)
            select_declaratie = Select(tip_declaratie_elem)
            select_declaratie.select_by_visible_text("Declaratie de avere")

            locatie_elem = driver.find_element("id", LOCALITATE_INPUT_ID)
            select_locatie = Select(locatie_elem)
            select_locatie.select_by_index(localitate_index)

            search_declaratii_integritate(driver)
            descarca_declaratii_integritate(driver)

        current_start_date += datetime.timedelta(days=1)


@call_decorator
def open_advanced_search_page(driver):
    # Open advanced settings page
    buton_cautare_avansata_elem = driver.find_element("id", CAUTARE_AVANSATA_BUTON_ID)
    buton_cautare_avansata_elem.click()
    # Wait for elements to load
    try:
        element_present = EC.presence_of_element_located(("id", NUME_PRENUME_INPUT_ID))
        WebDriverWait(driver, LOADING_TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for advanced search page to load")


@call_decorator
def scrape(args):
    driver = get_selenium_driver()
    driver.get(args.website)
    if args.website == DECLARATII_INTEGRITATE_WEBSITE:
        scrape_declaratii_integritate(driver)
    input('Type something if you want to close the browser\n')


if __name__ == '__main__':
    arg_parser = get_parser()
    args = arg_parser.parse_args()
    scrape(args)
