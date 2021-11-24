from tests.acceptance.locators.base_page import BasePageLocators


# base page tüm pagelerin sahip olması gereken şeyleri tutar
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000/'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)
