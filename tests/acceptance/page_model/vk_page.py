from selenium.webdriver.common.by import By
import time


class VkPage:
    def __init__(self,driver):
        self.driver=driver

    @property
    def url(self):
        return 'https://vk.com/'




    @property
    def size_yardimci_sevindik(self):
        return self.driver.find_element(By.XPATH,'//div[contains(text(),"Size")]')

    @property
    def myproblemsolvedbutton(self):
        return self.driver.find_element(By.XPATH,'//span[@class="help_table_question_act help_table_question_act_ok"]')


    @property
    def howdohidelistclick(self):
        return self.driver.find_element(By.XPATH,'//div[text()="How do I hide my profile from other users?"]')
    @property
    def hideheader(self):
        return self.driver.find_element(By.XPATH,'//h1[text()="How do I hide my profile from other users?"]')


    @property
    def soruyugiriniz_text(self):
        return self.driver.find_element(By.XPATH,'//input[@placeholder="Soruyu giriniz"]')
    @property
    def sabanci_input_text(self):
        return self.driver.find_element(By.XPATH,'//input[@class="ui_search_field _field"]')

    @property
    def enter_web_link(self):
        return self.driver.find_element(By.XPATH,'//input[@aria-label="Videoya link"]')
    @property
    def save_button_video_link(self):
        return self.driver.find_elements(By.XPATH,'//button[@class="flat_button"]')


    @property
    def add_from_another_site(self):
        return self.driver.find_element(By.XPATH,'//button[text()="Başka siteden eklemek"]')

    @property
    def add_video_upload(self):
        return self.driver.find_elements(By.XPATH,'//button[text()="Video ekle"]')


    @property
    def video_find_left(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Video"]')

    @property
    def my_video_recordings(self):
        return self.driver.find_element(By.XPATH,'//a[@class="ui_tab"]')

    @property
    def open_website(self):
        return self.driver.find_element(By.XPATH,'//button[text()="Siteyi aç"]')

    @property
    def website_open(self):
        return self.driver.find_element(By.XPATH,'//button[text()="Siteyi aç"]')


    @property
    def abone_oldunuz_message(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Siz abone oldunuz"]')


    @property
    def zenit_text_click(self):
        return self.driver.find_element(By.XPATH,'//a[text()="ФК «Зенит»"]')


    @property
    def abone_ol_zenit(self):
        return self.driver.find_elements(By.XPATH,'//button[text()="Abone ol"]')


    @property
    def topluluk_area_button(self):
        return self.driver.find_element(By.XPATH,'//button[@aria-label="Topluluk ara"]')


    @property
    def topluluk_input_text(self):
        return self.driver.find_element(By.XPATH,'//input[@class="ui_search_field _field"]')

    @property
    def topluluk_arama_click(self):
        return self.driver.find_elements(By.XPATH,'//a[@href="/groups?act=catalog"]')


    @property
    def click_to_topluluk(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Topluluk"]')


    @property
    def share_post_ser(self):
        return self.driver.find_element(By.XPATH,'//button[@class="like_share_btn flat_button"]')


    @property
    def click_my_duvar(self):
        return self.driver.find_element(By.XPATH,'//div[@id="like_share_my"]')


    @property
    def share_post_button(self):
        return self.driver.find_element(By.XPATH,'//*[@id="post654156585_3"]/div/div[2]/div/div[2]/div/div[1]/a[3]/div[1]')


    @property
    def show_the_comments(self):
        return self.driver.find_element(By.XPATH,'//a[@id="ui_rmenu_comments"]')



    @property
    def reply_button_comment(self):
        return self.driver.find_element(By.XPATH,'//button[@class="reply_send_button"]')


    @property
    def comment_to_post_write(self):
        return self.driver.find_element(By.XPATH,'//div[@role="textbox"]')


    @property
    def comment_to_post(self):
        return self.driver.find_element(By.XPATH,'//a[@title="Yorum"]')


    @property
    def name_like_history(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Ali Tunceli"]')

    @property
    def like_buttons_history(self):
        return self.driver.find_element(By.XPATH,'//a[@href="/feed?section=likes"]')


    @property
    def svg_home_image(self):
        return self.driver.find_element(By.XPATH,'//a[@class="TopHomeLink"]')



    @property
    def like_button_post(self):
        return self.driver.find_element(By.XPATH,'//div[@class="like_button_icon"]')

    @property
    def black_list(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Kara liste"]')

    @property
    def black_list_member(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Ali Tunceli"]')


    @property
    def engelle_button_notificaton(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Kullanıcıyı kara listeden kaldır"]')

    @property
    def engelle_button(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Engelle"]')


    @property
    def continue_click_settings(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Devam"]')

    @property
    def logout_click(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Çıkış yap"]')


    @property
    def reklamlar_is_displayed(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Reklamlar"]')

    @property
    def save_button_menu_settings(self):
        return self.driver.find_element(By.XPATH,'//button[text()="Kaydet"]')


    @property
    def advertisements_click(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Reklamlar"]')


    @property
    def menu_members(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Menü elemanlarının görüntüsünü düzenle"]')


    @property
    def tosun_click_sagust(self):
        return self.driver.find_element(By.XPATH,'//a[@id="top_profile_link"]')

    @property
    def settings_click(self):
        return self.driver.find_element(By.XPATH,'//a[@href="/settings"]')

    @property
    def help_click(self):
        return self.driver.find_element(By.XPATH,'//a[@href="/support?act=home"]')


    @property
    def topnav_music(self):
        return self.driver.find_elements(By.XPATH,'//div[@class="TopNavBtn__icon"]')


    @property
    def music_date_displayed(self):
        return self.driver.find_element(By.XPATH,'//div[text()="2001"]')

    @property
    def music_name_displayed(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Опера #2"]')
    @property
    def search_button_music(self):
        return self.driver.find_element(By.XPATH,'//button[contains(@class,"ui_search_button_search")]')

    @property
    def muzik_ara_input(self):
        return self.driver.find_element(By.XPATH,'//input[@placeholder="Müzik ara"]')


    @property
    def musicButton(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Müzik"]')


    @property
    def talepname_sent(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Talepname gönderildi"]')


    @property
    def add_friends(self):
        return self.driver.find_element(By.XPATH,'//button[text()="Arkadaşlarıma ekle"]')

    @property
    def message_button(self):
        return self.driver.find_element(By.XPATH,'//button[text()="Mesaj yaz"]')
    @property
    def gonder_button(self):
        return self.driver.find_element(By.XPATH,'//button[text()="Gönder"]')
    @property
    def profile_name_true(self):
        return self.driver.find_element(By.XPATH,'//h1[text()="Ali  Tunceli"]')

    @property
    def enter_message_text(self):
        return self.driver.find_element(By.XPATH,'//div[@id="mail_box_editable"]')


    @property
    def click_the_name_search(self):
        return self.driver.find_element(By.XPATH,'//a[@href="/id654156585"]')


    @property
    def input_enter_search(self):
        return self.driver.find_element(By.XPATH,'//input[@placeholder="Arama"]')


    @property
    def save_button_change(self):
        return self.driver.find_element(By.XPATH,'//div[contains(@class,"Subhead Subhead--android")]')

    @property
    def change_name(self):
        return self.driver.find_element(By.XPATH,'//input[@value="Tosun"]')


    @property
    def vk_connect_enter(self):
        return self.driver.find_element(By.XPATH,'//a[@class="flat_button"]')

    @property
    def edit_name_displayed(self):
        return self.driver.find_element(By.XPATH,'//input[@value="Tosun"]')
    @property
    def edit_surname_displayed(self):
        return self.driver.find_element(By.XPATH,'//input[@value="Patlican"]')



    @property
    def edit_profile_page(self):
        return self.driver.find_element(By.XPATH,'//a[@id="profile_edit_act"]')

    @property
    def delete_post_button(self):
        return self.driver.find_element(By.XPATH,'//a[contains(@onclick,"delete")]')


    @property
    def delete_button_movetoElement(self):
        return self.driver.find_elements(By.XPATH,'//div[@class="ui_actions_menu_icons"]')

    @property
    def post_textinput(self):
        return self.driver.find_element(By.XPATH,'//div[@id="post_field"]')
    @property
    def publish_the_post(self):
        return self.driver.find_element(By.XPATH,'//button[@id="send_post"]')


    @property
    def city_display(self):
        return self.driver.find_element(By.XPATH,'//a[text()="İstanbul"]')

    @property
    def profileName(self):
        return self.driver.find_element(By.XPATH,'//h1[@class="page_name"]')

    @property
    def loginbutton_login(self):
        return self.driver.find_element(By.XPATH,'//button[@id="index_login_button"]')


    @property
    def myprofile_click(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Profilim"]')


    @property
    def sms_confirmation(self):
        return self.driver.find_element(By.XPATH,'//h4[text()="SMS confirmation"]')


    @property
    def give_phone_number(self):
        return self.driver.find_element(By.XPATH,'//input[@id="join_phone"]')
    @property
    def join_send_button(self):
        return self.driver.find_element(By.XPATH,'//button[@id="join_send_phone"]')

    @property
    def day_register(self):
        return self.driver.find_elements(By.XPATH,'//table[@class="selector_table"]')
    @property
    def day_click(self):
        return self.driver.find_element(By.XPATH,'//li[@onmousedown="Select.itemMouseDown(1, 11, this)"]')
    @property
    def man_gender_click(self):
        return self.driver.find_elements(By.XPATH,'//div[@class="radiobtn"]')
    @property
    def continue_click(self):
        return self.driver.find_element(By.XPATH,'//button[contains(@class," button_big_text ij_button")]')


    @property
    def month_click(self):
        return self.driver.find_element(By.XPATH,'//li[@title="April"]')
    @property
    def year_click(self):
        return self.driver.find_element(By.XPATH,'//li[@val="2001"]')


    @property
    def register_surname(self):
        return self.driver.find_element(By.XPATH,'//input[@id="ij_last_name"]')


    @property
    def register_name(self):
        return self.driver.find_element(By.XPATH,'//input[@id="ij_first_name"]')

    @property
    def get_email(self):
        return self.driver.find_element(By.XPATH,'//input[@id="index_email"]')

    @property
    def get_password(self):
        return self.driver.find_element(By.XPATH,'//input[@id="index_pass"]')
    @property
    def button_click(self):
        return self.driver.find_element(By.XPATH,'//button[@id="index_login_button"]')
