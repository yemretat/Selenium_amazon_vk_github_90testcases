import time

from tests.acceptance.locators.sucourse_loc import SuCoursePageLocators
from selenium.webdriver.common.by import By


class SuCoursePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def hiddendivbadges(self):
        return self.driver.find_element(By.XPATH,'//div[@class="block_badges block hidden"]')

    @property
    def nobadges(self):
        return self.driver.find_element(By.XPATH,'//div[text()="You have no badges to display"]')

    @property
    def latest_badges_button(self):
        return self.driver.find_elements(By.XPATH,'//div[@class="block_action"]')

    @property
    def announcement_forum(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Announcements Forum"]')


    @property
    def sucourseplus(self):
        return self.driver.find_elements(By.XPATH,'//span[text()="SUCourse vs SUCourse+"]')


    @property
    def google_doc(self):
        return self.driver.find_element(By.XPATH,'//a[text()="into this google doc"]')


    @property
    def su_orientations(self):
        return self.driver.find_elements(By.XPATH,'//span[text()="SU Orientation"]')


    @property
    def sucourse_tutorials_links(self):
        return self.driver.find_element(By.XPATH,'//a[text()="SUCourse Tutorials"]')

    @property
    def get_calendar_url(self):
        return self.driver.find_element(By.XPATH,'//input[@value="Get calendar URL"]')
    @property
    def time_period_radios(self):
        return self.driver.find_elements(By.XPATH,'//input[@name="period[timeperiod]"]')


    @property
    def all_events_radio(self):
        return self.driver.find_element(By.XPATH,'//input[@id="id_events_exportevents_all"]')


    @property
    def export_calendar_button(self):
        return self.driver.find_element(By.XPATH,'//button[text()="Export calendar"]')


    @property
    def go_to_calendar(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Go to calendar..."]')


    @property
    def elae_exam_login(self):
        return self.driver.find_element(By.XPATH,'//a[text()="ELAE exam login"]')

    @property
    def invalid_loginpleasetry(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Invalid login, please try again"]')

    @property
    def login_button_guest(self):
        return self.driver.find_element(By.XPATH,'//input[@id="loginbtn"]')

    @property
    def password_guestuser(self):
        return self.driver.find_element(By.XPATH,'//input[@autocomplete="current-password"]')


    @property
    def username_guestuser(self):
        return self.driver.find_element(By.XPATH,'//input[@autocomplete="username"]')


    @property
    def guestusers(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Guest users"]')

    @property
    def noupcomingactivities(self):
        return self.driver.find_elements(By.XPATH,'//p[text()="No upcoming activities due"]')

    @property
    def sortByCourses(self):
        return self.driver.find_element(By.XPATH,'//a[@href="#myoverview_timeline_courses"]')

    @property
    def timeline_tabname(self):
        return self.driver.find_element(By.XPATH,'//a[@data-tabname="timeline"]')

    @property
    def courses_tabname(self):
        return self.driver.find_element(By.XPATH,'//a[@data-tabname="courses"]')


    @property
    def nobadges_alert(self):
        return self.driver.find_element(By.XPATH,'//button[@data-dismiss="alert"]')

    @property
    def manage_badges(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Manage badges"]')
    @property
    def preferences_click(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Preferences"]')

    @property
    def yunusemretatrightupper(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Yunus Emre Tat"]')

    @property
    def cs439displayed(self):
        return self.driver.find_element(By.XPATH,'//h2[text()="Search results: 1"]')

    @property
    def search_courses(self):
        return self.driver.find_element(By.XPATH,'//input[@value="Search courses"]')

    @property
    def search_button_main(self):
        return self.driver.find_element(By.XPATH,'//button[@type="submit"]')

    @property
    def gr55e(self):
        return self.driver.find_element(By.XPATH,'//a[text()="GR555E-202002"]')


    @property
    def ikiyirmispring(self):
        return self.driver.find_element(By.XPATH,'//a[contains(text(),"2020 - 2021 Spring")]')

    @property
    def lefteki_courses(self):
        return self.driver.find_element(By.XPATH,'//a[text()="Courses"]')

    @property
    def url(self):
        return 'https://sucourse.sabanciuniv.edu/plus/'

    @property
    def welcome_sabanci(self):
        return self.driver.find_element(By.XPATH,'//h1[text()="Welcome to Sabancı University"]')


    @property
    def close_button_site_home(self):
        return self.driver.find_elements(By.XPATH,'//button[@title="Close"]')



    @property
    def site_home(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Site home"]')

    @property
    def click_side_bar(self):
        return self.driver.find_element(By.XPATH,'//div[@id="sidebar-btn"]')

    @property
    def invalid_credentials(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Invalid credentials."]')

    @property
    def send_message_button(self):
        return self.driver.find_element(By.XPATH,'//button[@data-action="send-message"]')
    @property
    def send_message_textarea(self):
        return self.driver.find_element(By.XPATH,'//textarea[@data-region="send-message-txt"]')
    @property
    def click_user_to_message(self):
        return self.driver.find_element(By.XPATH,'//div[@class="information"]')
    @property
    def searchtext(self):
        return self.driver.find_element(By.XPATH,'//input[@id="searchtext"]')
    @property
    def create_Contacts(self):
        return self.driver.find_element(By.XPATH,'//div[text()="Contacts"]')

    @property
    def new_Message_creation(self):
        return self.driver.find_element(By.XPATH,'//a[contains(@href,"message/index.php?contactsfirst=1")]')

    @property
    def messages_icon(self):
        return self.driver.find_element(By.XPATH,'//img[@alt="Toggle messages menu"]')

    @property
    def select_file_managment(self):
        return self.driver.find_element(By.XPATH,'//button[text()="Select this file"]')
    @property
    def sabiha_click(self):
        return self.driver.find_element(By.XPATH,'//p[text()="sabihagökçen.txt"]')

    @property
    def moodle_org(self):
        return self.driver.find_element(By.XPATH,'//a[@href="https://moodle.org/"]')


    @property
    def file_picker_files(self):
        return self.driver.find_element(By.XPATH,'//span[text()="Recent files"]')
    @property
    def upload_manage_files(self):
        return self.driver.find_elements(*SuCoursePageLocators.UPLOAD_FILES_MANAGEFILES)
    @property
    def manage_private_files(self):
        return self.driver.find_element(*SuCoursePageLocators.MANAGE_PRIVATE_FILES)
    @property
    def select_dropdownoptions(self):
        return self.driver.find_elements(*SuCoursePageLocators.SELECT_DROPDOWN_OPTIONS)
    @property
    def event_Save(self):
        return self.driver.find_element(*SuCoursePageLocators.SAVE_EVENT_BUTTON)
    @property
    def input_name(self):
        return self.driver.find_element(*SuCoursePageLocators.INPUT_NAME)
    @property
    def new_event_button(self):
        return self.driver.find_element(*SuCoursePageLocators.NEW_EVENT)

    @property
    def sucourse_months(self):
        return self.driver.find_elements(*SuCoursePageLocators.CALENDARS)
    @property
    def user_blog_name(self):
        return self.driver.find_element(*SuCoursePageLocators.BLOG_NAME_DISPLAY)
    @property
    def save_changes_blog(self):
        return self.driver.find_element(*SuCoursePageLocators.SUBMIT_BUTTON)

    @property
    def blog_entry_body(self):
        return self.driver.find_element(*SuCoursePageLocators.BLOG_ENTRY_BODY)

    @property
    def entry_title(self):
        return self.driver.find_element(*SuCoursePageLocators.BLOG_TITLE)

    @property
    def add_new_entry(self):
        return self.driver.find_element(*SuCoursePageLocators.ADD_NEW_ENTRY)

    @property
    def Blog_entries_button(self):
        return self.driver.find_element(*SuCoursePageLocators.BLOG_ENTRIES)

    @property
    def profile_name_sucourse(self):
        return self.driver.find_element(*SuCoursePageLocators.USER_PROFILE_NAME)
    @property
    def update_pro(self):
        return self.driver.find_element(*SuCoursePageLocators.UPDATE_PROFILE)
    @property
    def first_name_phonetic(self):
        return self.driver.find_element(*SuCoursePageLocators.EDIT_PROFILE_FIRST_NAME)
    @property
    def additional_names(self):
        return self.driver.find_element(*SuCoursePageLocators.ADDITIONAL_NAMES)

    @property
    def edit_profile(self):
        return self.driver.find_elements(*SuCoursePageLocators.EDIT_PROFILE)

    @property
    def image_links(self):
        return self.driver.find_elements(*SuCoursePageLocators.USER_IMAGES)
    @property
    def post_to_form(self):
        return self.driver.find_element(*SuCoursePageLocators.POST_TO_FORUM)

    @property
    def reply_the_discussion(self):
        return self.driver.find_elements(*SuCoursePageLocators.REPLY_DISCUSSION)
    @property
    def enter_message(self):
        enter_message=self.driver.find_element(*SuCoursePageLocators.DISCUSSION_REPLY)
        time.sleep(2)
        return enter_message
    @property
    def discussion_topic(self):
        return self.driver.find_elements(*SuCoursePageLocators.DISCUSSION_BOARD_TOPIC)
    @property
    def discussion_board(self):
        return self.driver.find_elements(*SuCoursePageLocators.DISCUSSION_BOARD)

    @property
    def sucourse_forum(self):
        return self.driver.find_element(*SuCoursePageLocators.SUCOURSE_FORM)

    @property
    def activities_page(self):
        return self.driver.find_elements(*SuCoursePageLocators.ACTIVITIES_CONTENT)

    @property
    def dropdown_cs439(self):
        return self.driver.find_elements(*SuCoursePageLocators.DROPDOWN_CS439)

    @property
    def dropdown_mycourses(self):
        return self.driver.find_element(*SuCoursePageLocators.MY_COURSES_DROPDOWN)

    @property
    def name_displayed(self):
        return self.driver.find_element(*SuCoursePageLocators.SUCOURSE_NAME_DISPLAY)

    @property
    def login_submit(self):
        return self.driver.find_element(*SuCoursePageLocators.LOGIN_SUBMIT)

    @property
    def login_username(self):
        return self.driver.find_element(*SuCoursePageLocators.LOGIN_USERNAME_TEXT)

    @property
    def login_password(self):
        login_pass= self.driver.find_element(*SuCoursePageLocators.LOGIN_PASSWORD)
        time.sleep(1)
        return login_pass

    @property
    def login_button(self):
        return self.driver.find_element(*SuCoursePageLocators.LOGIN_SUCOURSE)

    @property
    def login_button_2(self):
        return self.driver.find_element(*SuCoursePageLocators.LOGIN_SUCOURSE2)