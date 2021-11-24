import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from tests.acceptance.page_model.sucourse_page import SuCoursePage

use_step_matcher('re')
@when('Hidden badges are displayed')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    page.hiddendivbadges.is_displayed()


@when('Badges are displayed')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    page.nobadges.is_displayed()

@when('I click the latest badges')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    page.latest_badges_button[3].click()

@when('I click the announcements forum')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.announcement_forum.click()

@when('I click the sucourseplus')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    page.sucourseplus[0].click()


@when('I click the google doc')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.google_doc.click()
    context.browser.switch_to_window(context.browser.window_handles[2])
    time.sleep(3)


@when('I click the su orientation tab')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.su_orientations[0].click()

@when('I click the useful link sucourse tutorial')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.sucourse_tutorials_links.click()
    context.browser.switch_to_window(context.browser.window_handles[1])

@when('I click the get calendar url')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.get_calendar_url.click()

@when('I click time period all events')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.time_period_radios[0].click()

@when('I click all events type form')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.all_events_radio.click()


@when('I click the export calendar button')
def step_impl(context):
    time.sleep(2)
    context.browser.execute_script("window.scrollBy(0,500)", "")
    page=SuCoursePage(context.browser)
    page.export_calendar_button.click()


@when('I click the go to calendar')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.go_to_calendar.click()

@when('I click the ELAE exam login')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.elae_exam_login.click()

@when('Invalid login notification displayed')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.invalid_loginpleasetry.is_displayed()

@when('I login button guest account')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.login_button_guest.click()

@when('I enter the password guest account')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.password_guestuser.send_keys("Sucourse1999")

@when('I enter username guest account')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.username_guestuser.send_keys("tatyunus")

@when('I click the Guest users')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.guestusers.click()

@when('No upcoming activities due content')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.noupcomingactivities[5].is_displayed()
@when('I click the timeline tabs')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.timeline_tabname.click()

@when('I click the courses tabs')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.courses_tabname.click()

@when('I click the manage badges')
def step_impl(context):
    time.sleep(1)
    page=SuCoursePage(context.browser)
    page.manage_badges.click()

@when('I click the yunus emre tat preferences')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.preferences_click.click()

@when('I click the yunus emre tat')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.yunusemretatrightupper.click()



@when('I click the user preferences edit sucourse')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.edit_profile[2].click()


@when('I enter the Cs439')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.search_courses.send_keys("Cs439")

@when('I click the searching button')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.search_button_main.click()

@when('I select the searching button')
def step_impl(context):
    page=SuCoursePage(context.browser)
    search=page.search_button_main
    action = ActionChains(context.browser)
    action.move_to_element(search).perform()

@when('I click gre555e button')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.gr55e.click()

@when('I click the 2020-2021 Spring')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.ikiyirmispring.click()

@when('I click the courses in navbar')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.lefteki_courses.click()
    time.sleep(2)
@when('I click the close button')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    page.close_button_site_home[0].click()
    time.sleep(1)



@when('I click the site home in sidebar')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.site_home.click()
    time.sleep(1)
@when('I click the sidebar-btn left part')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.click_side_bar.click()
    time.sleep(2)


@when('I click the send message button')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.send_message_button.click()

@when('I enter the "(.*)" message to send message text area')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    time.sleep(3)
    page.send_message_textarea.send_keys(content)

@when('I click the user which I write to text')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.click_user_to_message.click()


@when('I write the "(.*)" text to the input')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    page.searchtext.send_keys(content)
    time.sleep(2)
@when('I click the contact image')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.create_Contacts.click()
    time.sleep(2)

@when('I click the new messages to create')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.new_Message_creation.click()
    time.sleep(1)

@when('I click the messages icon')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.messages_icon.click()
    time.sleep(2)

@when('I click the select file in management')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.select_file_managment.click()

@when("Click the moodle org useful links")
def step_impl(context):
    page=SuCoursePage(context.browser)
    context.browser.execute_script("window.scrollBy(0,2700)", "")
    time.sleep(3)
    page.moodle_org.click()
    context.browser.switch_to_window(context.browser.window_handles[1])


@when('I click a file in file picker')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    page.sabiha_click.click()
@when('I select the select this file button')
def step_impl(context):
    time.sleep(1)
    page=SuCoursePage(context.browser)
    page.select_this_file.click()

@when('I select the files from file picker popup')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    page.file_picker_files.click()

@when('I click the upload files management')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    page.upload_manage_files[0].click()

@when('I click the manage private files')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.manage_private_files.click()

@when('I click the save event button')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.event_Save.click()

@when('I enter the "(.*)" name to name input')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    page.input_name.send_keys(content)


@when('I click the new event button')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.new_event_button.click()
    time.sleep(2)

@when('I clicked months in the calendar')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    context.browser.execute_script("window.scrollBy(0,400)", "")
    page.sucourse_months[0].click()

@when('I click the save changes in the blog page')
def step_impl(context):
    page=SuCoursePage(context.browser)
    context.browser.execute_script("window.scrollBy(0,1200)", "")

    page.save_changes_blog.click()

@when('I entry the blog entry body as "(.*)"')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    page.blog_entry_body.send_keys(content)


@when('I entry the entry title name as "(.*)"')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    page.entry_title.send_keys(content)


@when('I add the new entry to blog posts')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.add_new_entry.click()



@when('I click the blog entries button')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.Blog_entries_button.click()


@when('I click the update profile button')
def step_impl(context):
    context.browser.execute_script("window.scrollBy(0,200)", "")

    page=SuCoursePage(context.browser)
    page.update_pro.click()

@when('I enter the "(.*)" name')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    page.first_name_phonetic.send_keys(content)
@when('I click the additional names')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.additional_names.click()

@when('I click the user profile edit sucourse')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.edit_profile[1].click()

@when('I click the user profile image sucourse')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.image_links[1].click()

@when('I click the post to forum')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.post_to_form.click()


@when('Enter the "(.*)" message to the discussion')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    print("BABA")
    messagebox=page.enter_message
    print("BABA2")

    time.sleep(2)
    print("BABA3")
    print(content)
    messagebox.send_keys(content)

@when('I click the reply the discussion')
def step_impl(context):
    page = SuCoursePage(context.browser)
    context.browser.execute_script("window.scrollBy(0,300)", "")

    page.reply_the_discussion[0].click()
    time.sleep(3)
@when('I click the discussion board page')
def step_impl(context):
    page = SuCoursePage(context.browser)
    page.discussion_topic[1].click()

@when('I click the discussion board')
def step_impl(context):
    page = SuCoursePage(context.browser)
    page.discussion_board[0].click()

@when('I click the form on sucourse')
def step_impl(context):
    page = SuCoursePage(context.browser)
    page.sucourse_forum.click()

@when('I select the My courses actions')
def step_impl(context):
    page = SuCoursePage(context.browser)
    action=ActionChains(context.browser)
    action.move_to_element(page.dropdown_mycourses).perform()
    time.sleep(2)
    page.dropdown_cs439[1].click()

@when('I click the SuCourse submit login button')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.login_submit.click()

@when('I give the login password as "(.*)"')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    page.login_password.send_keys(content)

@when('I give the login name as "(.*)"')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    page.login_username.send_keys(content)

@when("I click the SuCourse login button2")
def step_impl(context):
    page = SuCoursePage(context.browser)
    page.login_button_2.click()


@when("I click the SuCourse login button")
def step_impl(context):
    page = SuCoursePage(context.browser)
    page.login_button.click()


