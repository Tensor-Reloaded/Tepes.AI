# import os
# import time
#
# import argparse
#
# downloadPath=r"E:\crawler-taip\declaratii"
# options = webdriver.ChromeOptions()
# prefs = {}
# try:
#     os.makedirs(downloadPath)
# except:
#     pass
# prefs["profile.default_content_settings.popups"]=0
# prefs["download.default_directory"]=downloadPath
# options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(executable_path="./driver/chromedriver", options=options)
#
# url = r"http://declaratii.integritate.eu/search.html"
#
# if __name__ == "__main__":
#     driver.get(url)
#     button = driver.find_element_by_id('form:showAdvancedSearch')
#     button.click()
#     time.sleep(5)
#     nume_prenume = driver.find_element_by_id('form:NumePrenume_input')
#     nume_prenume.send_keys("mosor")
#     submit_button = driver.find_element_by_id('form:submitButtonAS')
#     time.sleep(1)
#     submit_button.click()
#     time.sleep(5)
#     for i in range(3):
#         row = driver.find_element_by_id(f"form:resultsTable_row_{i}")
#         for p in row.find_elements_by_css_selector("*"):
#             if p.text == "Vezi document":
#                 p.click()
#                 time.sleep(1)
#                 print(p.id, p.text)
#         # download_button = row.find_element_by_class_name(r"null ui-col-7 ui-datatable-first")
#         # download_button.click()
import os.path

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import *
from declaration_parser import get_parser


def get_selenium_driver():
    DECLARATIONS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "declarations")
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': DECLARATIONS_PATH}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', prefs)
    return webdriver.Chrome(executable_path=LOCATIE_DRIVER, options=options)


def fill_detalii_declaratii_integritate(driver, args):
    # Open advanced settings page
    buton_cautare_avansata_elem = driver.find_element("id", CAUTARE_AVANSATA_BUTON_ID)
    buton_cautare_avansata_elem.click()

    # Wait for elements to load
    try:
        element_present = EC.presence_of_element_located(("id", NUME_PRENUME_INPUT_ID))
        WebDriverWait(driver, LOADING_TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    if args.nume:
        nume_prenume_elem = driver.find_element("id", NUME_PRENUME_INPUT_ID)
        nume_prenume_elem.send_keys(args.nume)
    if args.prenume:
        nume_prenume_elem = driver.find_element("id", NUME_PRENUME_INPUT_ID)
        nume_prenume_elem.send_keys(' ' + args.prenume)
    if args.functii:
        functii = args.functii.split(',')
        functii_elem = driver.find_element("id", FUNCTIE_INPUT_ID)
        buton_add_functii_elem = driver.find_element("id", ADAUGA_FUNCTIE_BUTON_ID)
        for functie in functii:
            functii_elem.send_keys(functie)
            buton_add_functii_elem.click()
            functii_elem.clear()
    if args.data_inceput:
        data_inceput_elem = driver.find_element("id", DATA_INCEPUT_INPUT_ID)
        data_inceput_elem.send_keys(args.data_inceput)
    if args.data_sfarsit:
        data_sfarsit_elem = driver.find_element("id", DATA_SFARSIT_INPUT_ID)
        data_sfarsit_elem.send_keys(args.data_sfarsit)
    if args.judet:
        judet_elem = driver.find_element("id", JUDET_INPUT_ID)
        select_judet = Select(judet_elem)
        select_judet.select_by_visible_text(args.judet)
    if args.localitate:
        localitate_elem = driver.find_element("id", LOCALITATE_INPUT_ID)
        select_localitate = Select(localitate_elem)
        select_localitate.select_by_visible_text(args.localitate)
    if args.tip_declaratie:
        tip_declaratie_elem = driver.find_element("id", TIP_DECLARATIE_INPUT_ID)
        select_declaratie = Select(tip_declaratie_elem)
        select_declaratie.select_by_visible_text(args.tip_declaratie)


def search_declaratii_integritate(driver):
    buton_cauta_elem = driver.find_element("id", CAUTA_BUTON_ID)
    buton_cauta_elem.click()


def descarca_declaratii_integritate(driver, count):
    # Wait for elements to load
    try:
        element_present = EC.presence_of_element_located(("id", BODY_TABEL_ID))
        WebDriverWait(driver, LOADING_TIMEOUT).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    if not count:
        pass # TODO -> implement next page accessing and download all declarations
    else:
        body_tabel_elem = driver.find_element("id", BODY_TABEL_ID)
        for row in body_tabel_elem.find_elements("css selector", "*")[::2]: # Mergem din 2 in 2 ca imi dubleaza elementele for some reason
            print(row.text)
            if row.text == DESCARCA_DOCUMENT_BUTON_TEXT:
                row.click()


def crawl_declaratii_integritate(driver, args):
    fill_detalii_declaratii_integritate(driver, args)
    search_declaratii_integritate(driver)
    descarca_declaratii_integritate(driver, args.count)


def crawl(args):
    driver = get_selenium_driver()
    driver.get(args.website)
    if args.website == DECLARATII_INTEGRITATE_WEBSITE:
        crawl_declaratii_integritate(driver, args)
    input('Type something if you want to close the browser\n')


if __name__ == '__main__':
    arg_parser = get_parser()
    args = arg_parser.parse_args()
    crawl(args)
    print(args)
