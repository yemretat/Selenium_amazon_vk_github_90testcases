import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from tests.acceptance.page_model.sucourse_page import SuCoursePage

use_step_matcher('re')

@then('Cs439 is displayed')
def step_impl(context):
    time.sleep(3)
    page=SuCoursePage(context.browser)
    page.cs439displayed.is_displayed()


@then('I control the requireloginerror')
def step_impl(context):
    time.sleep(1)
    page=SuCoursePage(context.browser)
    page.gr55e.is_displayed()
@then('I control the welcome to Sabanci university')
def step_impl(context):
    time.sleep(1)
    page=SuCoursePage(context.browser)
    page.welcome_sabanci.is_displayed()

@then('Invalid Credentials is displayed')
def step_impl(context):
    time.sleep(2)
    page=SuCoursePage(context.browser)
    page.invalid_credentials.is_displayed()

@then('Term Courses Presented Correctly')
def step_impl(context):
    page=SuCoursePage(context.browser)
    options=page.select_dropdownoptions
    select_options=["1","2660","2661","2664","2670","2850"]
    flag=True
    for i in range(len(options)):
        print(options[i].get_attribute("value"))
        if options[i].get_attribute("value")!=select_options[i]:
            flag=False


@then('The user blog name is displayed correctly')
def step_impl(context):
    page=SuCoursePage(context.browser)
    page.user_blog_name.is_displayed()

@then('The profile name is displayed as "(.*)"')
def step_impl(context,content):
    page=SuCoursePage(context.browser)
    flag=False
    if content==page.profile_name_sucourse.text:
        flag=True
        assert flag


@then('Activities are displayed')
def step_impl(context):
    page = SuCoursePage(context.browser)
    activities_titles = ["Assignment", "Forum", "Questionnaire", "Quiz"]
    activities = page.activities_page
    count = 0
    for i in range(0, 4):
        print("Static {}".format(activities_titles[i]))
        print(activities[i].get_attribute("title"))
     #   print("Dynamic {}".format(activities[i].title))
        time.sleep(2)
        if activities_titles[i] == activities[i].get_attribute("title"):
            count += 1

    if (count == 4):
        assert True
