import datetime
import os.path
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from constants import *
from scraping_parser import get_parser


def get_selenium_driver():
    DECLARATIONS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "declarations")
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': DECLARATIONS_PATH}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', prefs)
    return webdriver.Chrome(executable_path=LOCATIE_DRIVER, options=options)


def search_declaratii_integritate(driver):
    buton_cauta_elem = driver.find_element("id", CAUTA_BUTON_ID)
    buton_cauta_elem.click()


def descarca_declaratii_integritate(driver, count):
    try:
        element_present = EC.presence_of_element_located(("id", BODY_TABEL_ID))
        WebDriverWait(driver, 5).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    # if not count:
    #     pass  # TODO -> implement next page accessing and download all declarations
    # else:
    #     body_tabel_elem = driver.find_element("id", BODY_TABEL_ID)
    #     for row in body_tabel_elem.find_elements("css selector", "*")[
    #                ::2]:  # Mergem din 2 in 2 ca imi dubleaza elementele for some reason
    #         print(row.text)
    #         if row.text == DESCARCA_DOCUMENT_BUTON_TEXT:
    #             row.click()


def scrape_declaratii_integritate(driver):
    open_advanced_search_page(driver)

    start_date = datetime.date(year=2020, month=10, day=30)
    end_date = datetime.date(year=2022, month=10, day=30)

    current_start_date = start_date
    while current_start_date <= end_date:
        current_end_date = current_start_date + datetime.timedelta(days=2)

        tip_declaratie_elem = driver.find_element("id", TIP_DECLARATIE_INPUT_ID)
        select_declaratie = Select(tip_declaratie_elem)
        select_declaratie.select_by_visible_text("Declaratie de avere")

        data_inceput_elem = driver.find_element("id", DATA_INCEPUT_INPUT_ID)
        data_inceput_elem.send_keys(current_start_date.strftime('%d.%m.%Y'))

        data_sfarsit_elem = driver.find_element("id", DATA_SFARSIT_INPUT_ID)
        data_sfarsit_elem.send_keys(current_end_date.strftime('%d.%m.%Y'))

        for localitate_index in range(1, 3167):
            try:
                element_present = EC.presence_of_element_located(("id", DATA_INCEPUT_INPUT_ID))
                WebDriverWait(driver, 3).until(element_present)
            except TimeoutException:
                print("Timed out waiting for page to load")

            locatie_elem = driver.find_element("id", LOCALITATE_INPUT_ID)
            select_locatie = Select(locatie_elem)
            select_locatie.select_by_index(localitate_index)

            search_declaratii_integritate(driver)
            descarca_declaratii_integritate(driver, 1)

        data_inceput_elem.clear()
        data_sfarsit_elem.clear()
        current_start_date += datetime.timedelta(days=1)


def open_advanced_search_page(driver):
    # Open advanced settings page
    buton_cautare_avansata_elem = driver.find_element("id", CAUTARE_AVANSATA_BUTON_ID)
    buton_cautare_avansata_elem.click()
    # Wait for elements to load
    try:
        element_present = EC.presence_of_element_located(("id", NUME_PRENUME_INPUT_ID))
        WebDriverWait(driver, LOADING_TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")


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
