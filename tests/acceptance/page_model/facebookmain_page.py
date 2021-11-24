from tests.acceptance.locators.facebookbase_page import FacebookBasePageLocators
from selenium.webdriver.common.by import By
from tests.acceptance.locators.facebookmain_page import FacebookMainPageLocators


# base page tüm pagelerin sahip olması gereken şeyleri tutar
class FacebookMainPage:
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
    def posteds(self):
        return self.driver.find_elements(*FacebookMainPageLocators.STRONG_LINKS)
    @property
    def liked_button(self):
        return self.driver.find_element(*FacebookMainPageLocators.LIKED_POST)

    @property
    def submit_button(self):
        return self.driver.find_element(*FacebookBasePageLocators.SUBMIT_BUTTON)

    def form_field(self, name):
        return self.form.find_element(By.NAME, name)
