import argparse
import os
import shutil
import unittest

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from components.crawler.declarationscrawler.constants import DECLARATII_INTEGRITATE_WEBSITE, NUME_PRENUME_INPUT_ID, \
    LOADING_TIMEOUT
from components.crawler.declarationscrawler.crawler import get_selenium_driver, fill_detalii_declaratii_integritate, \
    search_declaratii_integritate, descarca_declaratii_integritate
from components.crawler.declarationscrawler.declaration_parser import parse_args


class CrawlerTest(unittest.TestCase):
    def setUp(self):

        self.download_location = "temp_declaratii_dir"
        self.driver = get_selenium_driver(self.download_location)
        self.driver.get(DECLARATII_INTEGRITATE_WEBSITE)
        self.nume_input = "croitoru"
        self.prenume_input_valid = "ra"
        self.prenume_input_invalid = "r"

    def get_args(self, valid=True):
        if valid:
            return parse_args(
                [DECLARATII_INTEGRITATE_WEBSITE, "--nume", self.nume_input, "--prenume", self.prenume_input_valid, ])
        return parse_args(
            [DECLARATII_INTEGRITATE_WEBSITE, "--nume", self.nume_input, "--prenume", self.prenume_input_invalid, ])

    def test_fill_declaratii_integritate(self):
        fill_detalii_declaratii_integritate(self.driver, self.get_args())

        nume_prenume_elem = self.driver.find_element("id", NUME_PRENUME_INPUT_ID)
        nume_prenume_value = nume_prenume_elem.get_attribute("value")

        self.assertEqual(nume_prenume_value, self.nume_input + " " + self.prenume_input_valid)

    def test_search_declaratii_integritate_invalid(self):
        error_text = 'Căutarea întoarce mai mult de 10 000 de rezultate. Vă rugăm să mai rafinați termenii de căutare.'
        fill_detalii_declaratii_integritate(self.driver, self.get_args(valid=False))
        search_declaratii_integritate(self.driver)

        try:
            element_present = EC.presence_of_element_located(("id", "_t129"))
            WebDriverWait(self.driver, LOADING_TIMEOUT).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        error_popup_elem = self.driver.find_element("id", "_t129")
        error_popup_value = error_popup_elem.text
        self.assertEqual(error_text, error_popup_value)

    def test_search_declaratii_integritate_valid(self):
        fill_detalii_declaratii_integritate(self.driver, self.get_args())
        search_declaratii_integritate(self.driver)

        try:
            element_present = EC.presence_of_element_located(("id", "form:resultsTable"))
            WebDriverWait(self.driver, LOADING_TIMEOUT).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        table_elem = self.driver.find_element("id", "form:resultsTable")
        self.assertIsNotNone(table_elem)

    def test_descarca_declaratii_integritate(self):
        fill_detalii_declaratii_integritate(self.driver, self.get_args())
        search_declaratii_integritate(self.driver)


        os.mkdir(self.download_location)
        descarca_declaratii_integritate(self.driver, 5)

        fisiere = os.listdir(self.download_location)
        self.assertIsNotNone(fisiere)

        shutil.rmtree(self.download_location)




