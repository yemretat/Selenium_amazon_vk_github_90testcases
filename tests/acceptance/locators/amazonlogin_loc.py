from selenium.webdriver.common.by import By


class AmazonLoginPageLocators:
    TITLE = By.CLASS_NAME, 'login'
    LOGIN_LINK = By.NAME, 'login'
    SUBMIT_BUTTON = By.NAME, 'login'
    POST_FORM = By.TAG_NAME, 'form'
    COK_SATANLAR = By.CSS_SELECTOR, 'a[href="/gp/bestsellers?ref_=nav_cs_bestsellers_6bce5169359d4ca5bc88df01d2a80d70"]'
    TESLIMAT_ADRES = By.CSS_SELECTOR, 'span[id ="glow-ingress-line2"]'
    BEBEK_BEZI = By.XPATH, '//div[text()="Xiaomi Mi TV Stick 1080p Android TV Media Player, Siyah"]'
    BUY_NOW_BUTTON=By.CSS_SELECTOR,'input[id="buy-now-button"]'
    EMAIL_INPUT=By.CSS_SELECTOR,'input[type=email]'
    SELECT_BAR=By.CSS_SELECTOR,'select[id=address-ui-widgets-countryCode-dropdown-nativeId]'
    CHECK_BOX=By.CSS_SELECTOR,'input[type=checkbox]'
    THIRTY_DAY_FREE = By.XPATH , '//a[text()="30 gün boyunca ücretsiz dene"]'

    PRIME_GAMING=By.XPATH , '//div[text()="Prime Gaming"]'
    PRIME_GAMING_KESFET=By.XPATH , '//a[text()="Prime Gaming\'i keşfet"]'
    THIRTY_DAY_FREE_TO_START = By.XPATH , '//span[contains(text(),"30")]'
    THIRTY_DAY_FREE_TO_START_Two=By.XPATH ,'//span[@class="dv-overlay"]'
 #   AMAZON_THIRTY_DAY_FREE=By.CSS_SELECTOR ,'//span[text()="30 gün ücretsiz dene"]'
    AMAZON_THIRTY_DAY_FREE = By.XPATH, '//input[@class="a-button-input"]'
    AMAZON_NO_THANKS=By.XPATH,'//a[text()="Hayır, teşekkürler. Amazon Prime\'a şimdi üye olmak istemiyorum."]'
    FIRSATLARI_YAKALA = By.CSS_SELECTOR ,'a[title="Fırsatları yakala"]'
    PRIME_VIDEO = By.CSS_SELECTOR ,'img[alt="Prime Video"]'
    AMAZON_PRIMECONTENT= By.XPATH , '//p[contains(text(),"Ödüllü")]'
    MOVETOELEMENT = By.CSS_SELECTOR , 'a[data-csa-c-slot-id=nav-link-accountList]'
    KARIYER_A = By.CSS_SELECTOR ,'a[href="https://www.amazon.jobs"]'
    RECYCLE_A = By.CSS_SELECTOR ,'a[href="/gp/browse.html?node=22380263031&ref_=footer_disposal"]'
    AMAZON_SALES_A= By.CSS_SELECTOR , 'a[href="https://services.amazon.com.tr"]'
    COMMUNICATION_A = By.XPATH ,'//a[text()="İletişim"]'
    REACH_US=By.XPATH,'//span[text()="Bize Ulaşın"]'
    YOUTUBE_POPUP=By.CSS_SELECTOR , 'a[class="link  button button-type-primary button-theme-filled font-size-medium ember"]'
    CONTACT_US = By.XPATH , '//h1[contains(text(),"yardıma ihtiyaç")]'
    FREE_SHIPPING = By.XPATH , '//img[@alt="Bedava ve Hızlı kargo"]'
    AMAZON_APP = By.XPATH , '//a[text()="Amazon Mobil Uygulaması"]'
    BENEFITS= By.CSS_SELECTOR ,'a[href="/en/benefits"]'
    COMPUTER_NAVBAR = By.XPATH , '//a[text()="Bilgisayar"]'
    FIVEHUND_ABOVE = By.XPATH , '//span[text()="500 TL Üzeri"]'
    PAGE_PASS = By.XPATH ,'//a[contains( @href,"pg_2")]'
    DOWNLOAD_APP = By.XPATH , '//img[contains(@src,"Download_app_store")]'
    SEPETE_EKLE=By.XPATH, '//input[@id="add-to-cart-button"]'
    COMPLETE_SHOPPING =By.XPATH ,'//a[@id="hlb-ptc-btn-native"]'
    ADRESS_CHOOSE=By.XPATH , '//a[@id="nav-global-location-popover-link"]'
    ADDRESS_CONTENT =By.XPATH , '//input[@aria-label="Adresinizi görmek için giriş yapın"]'
    YUNUS_NAME = By.XPATH , '//span[text()="Yunus​"]'
    REGISTER_SELECT=By.XPATH , '//a[@id="nav-link-accountList"]'
    UYE_OLUN = By.XPATH , '//a[text()="Üye olun."]'
    GIRIS_YAP_HIDDEN =By.XPATH , '//span[text()="Giriş yap"]'
    LOGOUT_HIDDEN = By.XPATH , '//span[text()="Çıkış Yap"]'
    AMAZON_SEARCH_BAR = By.XPATH , '//input[@id="twotabsearchtextbox"]'
    SEARCH_SUBMIT = By.XPATH , '//input[@id="nav-search-submit-button"]'
    MIN_VALUE_INPUT = By.XPATH , '//input[@name="low-price"]'
    MIN_VALUE_GIT= By.XPATH , '//input[@class="a-button-input"]'
    THE_MIN_VALUES=By.XPATH , '//span[@class="a-price-whole"]'
    SEARCHED_PRODUCT = By.XPATH , '//span[@class="a-color-state a-text-bold"]'
    ORDERS_HIDDEN=By.XPATH , '//span[text()="Siparişlerim"]'
    ORDERS_MESSAGE=By.XPATH , '//div[@class="a-section a-spacing-top-medium a-text-center"]'
    MYACCOUNT_HIDDEN=By.XPATH , '//span[text()="Hesabım"]'
    SECURITY_LOGIN = By.XPATH , '//div[@data-card-identifier="SignInAndSecurity"]'
    ACCOUNT_UPDATE=By.XPATH ,'//span[@class="a-button a-button-span12 a-button-base"]'
    NAME_UPDATE=By.XPATH , '//input[@id="ap_customer_name"]'
    PRODUCTS = By.XPATH , '//div[@class="p13n-sc-truncate-desktop-type2 p13n-sc-truncated"]'
    CARD_NUMBER=By.XPATH ,'//span[@id="nav-cart-count"]'
    GO_TO_CARD = By.XPATH, '//a[@href="/gp/cart/view.html?ref_=nav_cart"]'
    CONTINUE_TO_SHOPPING = By.XPATH ,'//span[@id="sc-buy-box-ptc-button"]'
    MAKE_A_LIST=By.XPATH , '//span[text()="Liste Oluşturun"]'
    MAKE_A_LIST_BUTTON =By.XPATH ,'//input[@class="a-button-input a-declarative"]'
    MAKE_COMMENT_BUTTON =By.XPATH , '//a[@data-hook="write-review-button"]'
    POSTAL_CODE = By.CSS_SELECTOR ,'input[placeholder="Posta Kodu"]'
    POSTAL_CODE_BUTTON=By.XPATH, '//input[@aria-labelledby="free_same_day_zip_checker_button-announce"]'
    POSTAL_CODE_MESSAGE=By.XPATH ,'//p[contains(text(),"34912 Prime Aynı Gün Teslimat bölgesinde değil")]'
    AMAZON_RECYCLE=By.XPATH ,'//a[@class="inline-link"]'
    ELDAY_LINK = By.XPATH ,'//img[@title="Elday"]'
    ACCEPT_THE_COOKIES=By.XPATH ,'//input[@name="accept"]'
    AMAZON_LOGO = By.XPATH ,'//a[@href="/ref=nav_logo"]'
    VIEW_HISTORY=By.XPATH ,'//a[@class="a-size-small a-link-normal ybh-inline-edit-link"]'
    PRODUCT_TITLE=By.XPATH ,'//span[@id="productTitle"]'
    VIEW_HISTORY_PRODUCTS=By.XPATH ,'//div[@class="p13n-sc-truncate-desktop-type2 p13n-sc-truncated"]'
    SELECT_QUANTITY = By.XPATH , '//select[@name="quantity"]'
    CARD_DELETE=By.XPATH , '//input[@data-action="delete"]'
    COMPLETE_THE_SHOPPING=By.XPATH ,'//a[@id="hlb-ptc-btn-native"]'
    CART_IMAGE=By.XPATH ,'//a[@id="nav-cart"]'
    CARD_PRODUCT_NAMES=By.XPATH, '//span[@class="a-truncate-cut"]'
    SAVE_FOR_LATER=By.XPATH,'//input[@value="Daha sonrası için kaydet"]'
    SAVED_PRODUCTS=By.XPATH ,'//span[@class="a-truncate-full"]'
    PROFILE_NAMES =By.XPATH ,'//span[@class="a-profile-name"]'
    COMMENT_USER_PROFILE=By.XPATH ,'//span[@class="a-size-extra-large"]'
    ALL_NAV_BAR=By.XPATH ,'//span[@class="hm-icon-label"]'
    GO_TO_GARDEN =By.XPATH ,'//*[@id="hmenu-content"]/ul[1]/li[8]/a/i'
    BITKILER_TOHUMLAR = By.XPATH ,'//a[text()="Bitkiler, Tohumlar ve Soğanlar"]'
    BITKILER_TOHUMLAR2=By.XPATH,'//span[@class="a-size-base a-color-base apb-browse-refinements-indent-1 a-text-bold"]'
    SEARCH_DROPDOWN=By.XPATH,'//select[@id="searchDropdownBox"]'
    GIFT_CARD_UPLOAD=By.XPATH,'//a[@class="a-button-text bxc-button-text "]'
    GIFT_CODE_UPLOAD=By.XPATH ,'//input[@name="claimCode"]'
    ADD_GIFT=By.XPATH ,'//input[@name="applytoaccount"]'
    INVALID_GIFT=By.XPATH ,'//h4[@class="a-alert-heading"]'