import os
import time

from seleniumbase import BaseCase

class FirstPageTest(BaseCase):
    def test_landing_page(self):
        self.open("http://declaratii.integritate.eu/search.html")
        self.assert_element("#form\:showAdvancedSearch")

        self.scroll_to_top()
        self.save_screenshot("test_landing_page", "custom_screenshots")
    def test_advanced_search_page(self):
        self.open("http://declaratii.integritate.eu/search.html")
        self.click("#form\:showAdvancedSearch")
        self.assert_text("Căutare declarații de avere și interese", "#form\:advanced-search-panel_content > div > div.ca_top_name > h5")
        self.assert_element("#form\:NumePrenume_input")
        self.assert_element("#form\:autoComplete_input")
        self.assert_element("#form\:Fnc_input")
        self.assert_element("#form\:startDate_input")
        self.assert_element("#form\:endDate_input")
        self.assert_element("#form\:Judet_input")
        self.assert_element("#form\:Localitate_input")
        self.assert_element("#form\:Tip_input")
        self.assert_element("#form\:submitButtonAS")

        self.scroll_to("#form\:advanced-search-panel_content > div > div.ca_top_name")
        self.save_screenshot("test_advanced_search_page_empty_fields", "custom_screenshots")
    def test_search_result(self):
        self.open("http://declaratii.integritate.eu/search.html")
        self.click("#form\:showAdvancedSearch")
        self.type("#form\:startDate_input", "01.05.2022")
        self.type("#form\:endDate_input", "01.11.2022")
        self.select_option_by_text("#form\:Localitate_input", "Abram")
        self.select_option_by_text("#form\:Tip_input", "Declaratie de avere")

        self.scroll_to("#form\:advanced-search-panel_content > div > div.ca_top_name")
        self.save_screenshot("test_advanced_search_page_completed_fields", "custom_screenshots")

        self.click("#form\:submitButtonAS")

        self.assert_element("#form\:resultsTable")
        self.assert_element("#form\:dataExporter")
        self.assert_text("18", "#form\:_t86")
        self.assert_text("Exportă", "#form\:dataExporter > span > span")

        self.scroll_to("#form\:j_idt84_content")
        self.save_screenshot("test_search_result", "custom_screenshots")
    def test_download_csv(self):
        self.open("http://declaratii.integritate.eu/search.html")
        self.click("#form\:showAdvancedSearch")
        self.type("#form\:startDate_input", "01.05.2022")
        self.type("#form\:endDate_input", "01.11.2022")
        self.select_option_by_text("#form\:Localitate_input", "Abram")
        self.select_option_by_text("#form\:Tip_input", "Declaratie de avere")
        self.click("#form\:submitButtonAS")
        self.click("#form\:dataExporter")

        time.sleep(2)

        print("SeleniumBase download folder: " + self.get_browser_downloads_folder())
        print(os.listdir(self.get_browser_downloads_folder()))

        time.sleep(4)

