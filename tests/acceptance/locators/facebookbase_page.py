from selenium.webdriver.common.by import By


class FacebookBasePageLocators:
    TITLE = By.CLASS_NAME, 'login'
    LOGIN_LINK = By.NAME, 'login'
    SUBMIT_BUTTON = By.NAME, 'login'
    POST_FORM = By.TAG_NAME, 'form'
