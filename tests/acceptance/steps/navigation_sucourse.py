import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.acceptance.page_model.sucourse_page import SuCoursePage

use_step_matcher('re')



@when('I click the sort by courses')
def step_impl(context):
    page = SuCoursePage(context.browser)
    page.sortByCourses.click()

@then('There are no badges available')
def step_impl(context):
    page = SuCoursePage(context.browser)
    page.nobadges_alert.is_displayed()

@then('You can check the timeline navigation url')
def step_impl(context):
    flag = False
    if "timeline" in context.browser.current_url:
        flag = True
    assert flag

@then('I am on the google docs page')
def step_impl(context):
    flag=False
    time.sleep(5)
    if "docs" in context.browser.current_url:
        flag=True
    assert flag

@then('I am on the message creation page')
def step_impl(context):
    flag=False
    if "message" in context.browser.current_url:
        flag=True
    assert flag

@then('I am on the moodle web site')
def step_impl(context):
    flag=False
    if "moodle" in context.browser.current_url:
        flag=True
    assert flag


@then('I am on the management private files page')
def step_impl(context):
    flag=False
    if "user/files" in context.browser.current_url:
        flag=True
    assert flag



@then('I am on the calendar page')
def step_impl(context):
    flag=False
    if "calendar/" in context.browser.current_url:
        flag=True
    assert flag


@then('I am on the blog entries page')
def step_impl(context):
    flag = False
    if "plus/blog" in context.browser.current_url:
        flag = True
    assert flag

@then('I am on the sucourse profile page')
def step_impl(context):
    flag = False
    if "user/profile" in context.browser.current_url:
        flag = True
    assert flag


@then('I am on discussion board page')
def step_impl(context):
    flag = False
    if "view.php?f=4576" in context.browser.current_url:
        flag = True
    assert flag

@then('I am on the Forum Page')
def step_impl(context):
    flag = False
    if "forum" in context.browser.current_url:
        flag = True
    assert flag

@then('I am on the CS439 Course Page')
def step_impl(context):
    flag=False
    if "2670" in context.browser.current_url:
        flag=True
    assert flag

@then('I am on the Sucourse user profile')
def step_impl(context):
    page = SuCoursePage(context.browser)
    page.name_displayed.is_displayed()

@given('I am on the SuCourse Login Page')
def step_impl(context):
    options = Options()
    options.headless=True
    context.browser = webdriver.Chrome("C://Users//Murtaza//Desktop//Courses//2021Spring//Cs439//pythonProject_proj//chromedriver_win32//chromedriver.exe")
    page = SuCoursePage(context.browser)
    context.browser.get(page.url)
    context.browser.maximize_window()
    time.sleep(2)



