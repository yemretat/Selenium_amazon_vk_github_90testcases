from selenium.webdriver.common.by import By


class SuCoursePageLocators:
    LOGIN_SUCOURSE = By.XPATH, '//a[text()="Login"]'
    LOGIN_SUCOURSE2 = By.XPATH, '//a[text()="SUNet users (Sabancı University members)"]'
    LOGIN_USERNAME = By.XPATH, '//input[@id="username"]'
    LOGIN_USERNAME_TEXT = By.XPATH, '//input[@name="username"]'
    LOGIN_PASSWORD = By.XPATH, '//input[@name="password"]'
    LOGIN_SUBMIT = By.XPATH, '//input[@type="submit"]'
    SUCOURSE_NAME_DISPLAY = By.XPATH, '//span[@class="usertext mr-1"]'
    MY_COURSES_DROPDOWN = By.XPATH, '//a[@data-toggle="dropdown"]'
    DROPDOWN_CS439 = By.XPATH, '//a[@title="CS439-202002"]'
    ACTIVITIES_CONTENT = By.XPATH, '//ul[@class="unlist"]//li//div//a//img'
    SUCOURSE_FORM = By.XPATH, '//img[@alt="Forum"]'
    DISCUSSION_BOARD = By.XPATH, '//a[@href="view.php?f=4576"]'
    DISCUSSION_BOARD_TOPIC = By.XPATH, '//a[@href="https://sucourse.sabanciuniv.edu/plus/mod/forum/discuss.php?d=15874"]'
    REPLY_DISCUSSION = By.XPATH, '//a[text()="Reply"]'
    DISCUSSION_REPLY=By.XPATH,'//div[@id="id_messageeditable"]'
    POST_TO_FORUM=By.XPATH,'//input[@name="submitbutton"]'
    USER_IMAGES=By.XPATH,'//img[@alt="Picture of Yunus Emre Tat"]'
    EDIT_PROFILE=By.XPATH,'//a[text()="Edit profile"]'
    BLOG_ENTRIES=By.XPATH ,'//a[text()="Blog entries"]'
    ADDITIONAL_NAMES=By.XPATH,'//a[@aria-controls="id_moodle_additional_names"]'
    EDIT_PROFILE_FIRST_NAME=By.XPATH , '//input[@name="firstnamephonetic"]'
    UPDATE_PROFILE=By.XPATH,'//input[@name="submitbutton"]'
    USER_PROFILE_NAME=By.XPATH,'//h2[text()="Yunus Emre Tat"]'
    ADD_NEW_ENTRY=By.XPATH,'//a[text()="Add a new entry"]'
    BLOG_TITLE=By.XPATH,'//input[@name="subject"]'
    BLOG_ENTRY_BODY=By.XPATH,'//div[@id="id_summary_editoreditable"]'
    SUBMIT_BUTTON=By.XPATH,'//input[@name="submitbutton"]'
    BLOG_NAME_DISPLAY=By.XPATH,'//h2[text()="User blog: Yunus Emre Tat"]'
    CALENDARS=By.XPATH,'//a[@title="This month"]'
    NEW_EVENT=By.XPATH,'//button[@data-action="new-event-button"]'
    INPUT_NAME=By.XPATH,'//input[@name="name"]'
    SAVE_EVENT_BUTTON=By.XPATH,'//button[@class="btn btn-primary"]'
    SELECT_DROPDOWN_OPTIONS=By.XPATH,'//select[@class="select custom-select cal_courses_flt"]//option'
    MANAGE_PRIVATE_FILES=By.XPATH,'//a[text()="Manage private files..."]'
    UPLOAD_FILES_MANAGEFILES=By.XPATH,'//div[@class="dndupload-arrow"]'
    SELECT_THIS_FILE='//button[text()="Select this file"]'
    FILE_PICKER_VİEW='//img[contains(@src,"image.php/lambda/theme/1619111055/fp/view_icon_active")]'








