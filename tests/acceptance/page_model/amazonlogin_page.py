import time

from tests.acceptance.locators.amazonlogin_loc import AmazonLoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AmazonLoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://www.amazon.com.tr/'

    @property
    def invalid_gift(self):
        return self.driver.find_element(*AmazonLoginPageLocators.INVALID_GIFT)
    @property
    def gift_code_button(self):
        return self.driver.find_element(*AmazonLoginPageLocators.ADD_GIFT)
    @property
    def gift_code_upload(self):
        return self.driver.find_element(*AmazonLoginPageLocators.GIFT_CODE_UPLOAD)
    @property
    def gift_card_upload(self):
        return self.driver.find_elements(*AmazonLoginPageLocators.GIFT_CARD_UPLOAD)

    @property
    def search_drop_down(self):
        return self.driver.find_element(*AmazonLoginPageLocators.SEARCH_DROPDOWN)

    @property
    def bitkiler_tohumlar2(self):
        return self.driver.find_element(*AmazonLoginPageLocators.BITKILER_TOHUMLAR2)

    @property
    def bitkiler_tohumlar(self):
        return self.driver.find_element(*AmazonLoginPageLocators.BITKILER_TOHUMLAR)

    @property
    def go_to_garden(self):
        return self.driver.find_element(*AmazonLoginPageLocators.GO_TO_GARDEN)

    @property
    def navbar_all(self):
        return self.driver.find_element(*AmazonLoginPageLocators.ALL_NAV_BAR)
    @property
    def profile_names(self):
        return self.driver.find_elements(By.XPATH,'//span[@class="a-profile-name"]')
    @property
    def real_comment_user(self):
        return self.driver.find_element(*AmazonLoginPageLocators.COMMENT_USER_PROFILE)

    @property
    def saveforlater(self):
        return self.driver.find_elements(*AmazonLoginPageLocators.SAVE_FOR_LATER)

    @property
    def card_product_names(self):
        return self.driver.find_element(By.XPATH,'//i[@class="a-icon a-icon-addon sc-best-seller-badge"]')
    @property
    def saved_for_later_products(self):
        return self.driver.find_element(By.XPATH,'//i[@class="a-icon a-icon-addon sc-best-seller-badge"]')

    @property
    def selectQuantity(self):
        select_quantity=self.driver.find_element(*AmazonLoginPageLocators.SELECT_QUANTITY)
        return select_quantity
    @property
    def view_history_titles(self):
        product_titles=self.driver.find_elements(*AmazonLoginPageLocators.VIEW_HISTORY_PRODUCTS)
        return product_titles
    @property
    def added_product_title(self):
        title=self.driver.find_element(*AmazonLoginPageLocators.PRODUCT_TITLE)
        return title
    @property
    def view_history(self):
        view_hist=self.driver.find_element(*AmazonLoginPageLocators.VIEW_HISTORY)
        return view_hist
    @property
    def recycle_A(self):
        recycle_A = self.driver.find_element(*AmazonLoginPageLocators.RECYCLE_A)
        return recycle_A
    @property
    def amazon_logo(self):
        amazon_log=self.driver.find_element(*AmazonLoginPageLocators.AMAZON_LOGO)
        return amazon_log
    @property
    def elday_page(self):
        elday_page=self.driver.find_element(*AmazonLoginPageLocators.ELDAY_LINK)
        return elday_page
    @property
    def accept_cookies(self):
        accept_cookies_button=self.driver.find_element(*AmazonLoginPageLocators.ACCEPT_THE_COOKIES)
        return accept_cookies_button

    @property
    def recycle_links(self):
        recycle_inline_links=self.driver.find_elements(*AmazonLoginPageLocators.AMAZON_RECYCLE)
        return recycle_inline_links
    @property
    def make_a_list_button(self):
        make_alist=self.driver.find_elements(*AmazonLoginPageLocators.MAKE_A_LIST_BUTTON)
        time.sleep(3)
        return make_alist[2]
    @property
    def postal_code_message(self):
        postal_code_message=self.driver.find_element(*AmazonLoginPageLocators.POSTAL_CODE_MESSAGE)
        return postal_code_message
    @property
    def postal_code_button(self):
        button_code=self.driver.find_element(*AmazonLoginPageLocators.POSTAL_CODE_BUTTON)
        return button_code

    @property
    def enter_postalcode(self):
        postalCode =self.driver.find_element(*AmazonLoginPageLocators.POSTAL_CODE)
        return postalCode

    @property
    def free_shipping(self):
        free_shipping = self.driver.find_element(*AmazonLoginPageLocators.FREE_SHIPPING)
        return free_shipping

    @property
    def make_comment(self):
        comment=self.driver.find_element(*AmazonLoginPageLocators.MAKE_COMMENT_BUTTON)
        return comment

    @property
    def make_a_list(self):
        return self.driver.find_element(*AmazonLoginPageLocators.MAKE_A_LIST)

    @property
    def continue_to_marketing(self):
        return self.driver.find_element(*AmazonLoginPageLocators.CONTINUE_TO_SHOPPING)
    @property
    def press_to_card(self):
        return self.driver.find_element(*AmazonLoginPageLocators.GO_TO_CARD)

    def enterFormfield(self, name):
        print("The name is {}".format(name))
        return self.driver.find_element(By.NAME, name)
    @property
    def card_number(self):
        return self.driver.find_element(*AmazonLoginPageLocators.CARD_NUMBER)
    @property
    def card_delete(self):
        return self.driver.find_element(*AmazonLoginPageLocators.CARD_DELETE)
    @property
    def complete_shopping(self):
        return self.driver.find_element(*AmazonLoginPageLocators.COMPLETE_SHOPPING)
    @property
    def products_to_buy(self):
        return self.driver.find_elements(By.XPATH,'//div[@class="a-section a-spacing-mini"]')
    @property
    def new_name_update(self):
        return self.driver.find_element(*AmazonLoginPageLocators.NAME_UPDATE)
    @property
    def account_update_buttons(self):
        return self.driver.find_elements(*AmazonLoginPageLocators.ACCOUNT_UPDATE)
    @property
    def login_security(self):
        return self.driver.find_element(*AmazonLoginPageLocators.SECURITY_LOGIN)

    @property
    def myaccount_hidden(self):
        return self.driver.find_element(*AmazonLoginPageLocators.MYACCOUNT_HIDDEN)
    @property
    def orders_hidden(self):
        return self.driver.find_element(*AmazonLoginPageLocators.ORDERS_HIDDEN)


    @property
    def ordered_product_message(self):
        return self.driver.find_element(*AmazonLoginPageLocators.ORDERS_MESSAGE)

    @property
    def searched_product(self):
        return self.driver.find_element(*AmazonLoginPageLocators.SEARCHED_PRODUCT)

    @property
    def get_the_prices(self):
        prices=self.driver.find_elements(*AmazonLoginPageLocators.THE_MIN_VALUES)
        return prices

    @property
    def git_min_value(self):
        git_min= self.driver.find_element(*AmazonLoginPageLocators.MIN_VALUE_GIT)
        time.sleep(2)
        return git_min
    @property
    def enter_min_value_input(self):
        return self.driver.find_element(*AmazonLoginPageLocators.MIN_VALUE_INPUT)

    @property
    def search_submit(self):
        return self.driver.find_element(*AmazonLoginPageLocators.SEARCH_SUBMIT)

    @property
    def submit_Search(self):
        return self.driver.find_element(*AmazonLoginPageLocators.SEARCH_SUBMIT)




    @property
    def searchBar(self):
        searchBar= self.driver.find_element(*AmazonLoginPageLocators.AMAZON_SEARCH_BAR)
        return searchBar

    def idliButton(self, id):
        return self.driver.find_element(By.ID, id)

    @property
    def logout_hidden(self):
        return self.driver.find_element(*AmazonLoginPageLocators.LOGOUT_HIDDEN)
    @property
    def giris_yap_hidden(self):
        return self.driver.find_element(*AmazonLoginPageLocators.GIRIS_YAP_HIDDEN)

    @property
    def hidden_uye_olun(self):
        return self.driver.find_element(*AmazonLoginPageLocators.UYE_OLUN)

    @property
    def register_select(self):
        register_select=self.driver.find_element(*AmazonLoginPageLocators.REGISTER_SELECT)
        return register_select

    @property
    def addressContent(self):
        addressContent=self.driver.find_element(*AmazonLoginPageLocators.ADDRESS_CONTENT)
        return addressContent
    @property
    def name_displayed(self):
        name_account=self.driver.find_element(*AmazonLoginPageLocators.YUNUS_NAME)
        return name_account

    @property
    def appstore(self):
        appstoreimage=self.driver.find_element(*AmazonLoginPageLocators.DOWNLOAD_APP)
        time.sleep(2)
        return appstoreimage
    @property
    def page_passing(self):
        pg_2=self.driver.find_elements(*AmazonLoginPageLocators.PAGE_PASS)
        time.sleep(2)
        return pg_2
    @property
    def address_Choose(self):
        address=self.driver.find_element(*AmazonLoginPageLocators.ADRESS_CHOOSE)
        return address
    @property
    def amazon_app(self):
        page_amazon_app=self.driver.find_element(*AmazonLoginPageLocators.AMAZON_APP)
        time.sleep(2)
        return page_amazon_app

    @property
    def fivehundred_above(self):
        fivehund=self.driver.find_element(*AmazonLoginPageLocators.FIVEHUND_ABOVE)
        time.sleep(1)
        return fivehund

    @property
    def computer_navbar(self):
        return self.driver.find_element(*AmazonLoginPageLocators.COMPUTER_NAVBAR)

    @property
    def benefits_href(self):
        benefits=self.driver.find_element(*AmazonLoginPageLocators.BENEFITS)
        time.sleep(2)
        return benefits


    @property
    def kariyer_href(self):
        kariyer= self.driver.find_element(*AmazonLoginPageLocators.KARIYER_A)
        time.sleep(2)
        return kariyer
    @property
    def amazon_sales_href(self):
        sales_in_amazon=self.driver.find_element(*AmazonLoginPageLocators.AMAZON_SALES_A)
        return sales_in_amazon
    @property
    def contact_us(self):
        contact_us = self.driver.find_element(*AmazonLoginPageLocators.CONTACT_US)
        return contact_us


    @property
    def communication_href(self):
        sales_in_amazon=self.driver.find_element(*AmazonLoginPageLocators.COMMUNICATION_A)
        return sales_in_amazon
    @property
    def reach_us_button(self):
        reach_us = self.driver.find_element(*AmazonLoginPageLocators.REACH_US)
        return reach_us

    @property
    def youtube_popup(self):
        return self.driver.find_elements(*AmazonLoginPageLocators.YOUTUBE_POPUP)
    @property
    def content_PrimeVideo(self):
        return self.driver.find_element(*AmazonLoginPageLocators.AMAZON_PRIMECONTENT)

    @property
    def account_movetoelement(self):
        return self.driver.find_element(*AmazonLoginPageLocators.MOVETOELEMENT)


    @property
    def prime_video(self):
        prime_videoe=self.driver.find_element(*AmazonLoginPageLocators.PRIME_VIDEO)
        time.sleep(2)
        return prime_videoe

    @property
    def firsatlari_yakala(self):
        firsatlar= self.driver.find_element(*AmazonLoginPageLocators.FIRSATLARI_YAKALA)
        time.sleep(2)
        return firsatlar
    @property
    def thirtday_free_try(self):
        return self.driver.find_elements(*AmazonLoginPageLocators.AMAZON_THIRTY_DAY_FREE)
    @property
    def dont_want_Amazon_prime(self):
        return self.driver.find_element(*AmazonLoginPageLocators.AMAZON_NO_THANKS)

    @property
    def thirtday_free_try_tostart(self):
        thirtday= self.driver.find_elements(*AmazonLoginPageLocators.THIRTY_DAY_FREE_TO_START_Two)
        return thirtday[1]
    @property
    def primegaming_start (self):
        return self.driver.find_element(*AmazonLoginPageLocators.PRIME_GAMING_KESFET)
    @property
    def primegaming_div(self):
        return self.driver.find_element(*AmazonLoginPageLocators.PRIME_GAMING)

    @property
    def textli_A(self):
        return self.driver.find_element(*AmazonLoginPageLocators.THIRTY_DAY_FREE)

    def selectCountry(self, country):
        select = self.driver.find_element(*AmazonLoginPageLocators.SELECT_BAR)
        return select
      #  print("It is okey ! ")
      #  print(drop)
      #  time.sleep(2)
      #  drop.select_by_index(1)
       # time.sleep(1)

        #drop.select_by_value("TC")

    def idliText(self, id):
        return self.driver.find_element(By.ID, id)


    @property
    def checkbox(self):
        return self.driver.find_element(*AmazonLoginPageLocators.CHECK_BOX)

    @property
    def sepeteEkle(self):
        return self.driver.find_element(*AmazonLoginPageLocators.SEPETE_EKLE)

    @property
    def complete_Shopping(self):
        return self.driver.find_element(*AmazonLoginPageLocators.COMPLETE_SHOPPING)

    @property
    def buyNowButton(self):
        return self.driver.find_element(*AmazonLoginPageLocators.BUY_NOW_BUTTON)
    @property
    def cart_image(self):
        return self.driver.find_element(*AmazonLoginPageLocators.CART_IMAGE)
    @property
    def cart_delete(self):
        return self.driver.find_elements(*AmazonLoginPageLocators.CARD_DELETE)


    @property
    def urlCokSatanlar(self):
        return 'https://www.amazon.com.tr/gp/bestsellers?ref_=nav_cs_bestsellers_6bce5169359d4ca5bc88df01d2a80d70'

    @property
    def tuvaletKagidiSatinAl(self):
        return self.driver.find_element(*AmazonLoginPageLocators.BEBEK_BEZI)

    @property
    def title(self):
        return self.driver.find_element(*AmazonLoginPageLocators.TESLIMAT_ADRES)

    @property
    def cok_satan_button(self):
        return self.driver.find_element(*AmazonLoginPageLocators.COK_SATANLAR)
