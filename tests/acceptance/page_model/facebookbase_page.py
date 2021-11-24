from tests.acceptance.locators.facebookbase_page import FacebookBasePageLocators
from selenium.webdriver.common.by import By


# base page tüm pagelerin sahip olması gereken şeyleri tutar
class FacebookBaseLoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://www.facebook.com/'

    @property
    def title(self):
        return self.driver.find_element(*FacebookBasePageLocators.LOGIN_LINK)

    @property
    def loginnavigation(self):
        return self.driver.find_elements(*FacebookBasePageLocators.LOGIN_LINK)

    @property
    def form(self):
        return self.driver.find_element(*FacebookBasePageLocators.POST_FORM)

    @property
    def submit_button(self):
        return self.driver.find_element(*FacebookBasePageLocators.SUBMIT_BUTTON)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)
