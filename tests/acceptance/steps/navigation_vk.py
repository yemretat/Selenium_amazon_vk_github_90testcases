from tests.acceptance.page_model.vk_page import  VkPage
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

use_step_matcher('re')


@then('Video Sabanci is displayed')
def step_impl(context):
    page=VkPage(context.browser)
    page.sabanci_input_text.is_displayed()

@then('Abone oldunuz message is displayed')
def step_impl(context):
    time.sleep(5)
    page=VkPage(context.browser)
    page.abone_oldunuz_message.is_displayed()
@then('Liked Ali Tunceli is displayed')
def step_impl(context):
    time.sleep(2)
    page=VkPage(context.browser)
    page.name_like_history.is_displayed()


@then('Black list member is visible')
def step_impl(context):
    time.sleep(3)
    page=VkPage(context.browser)
    page.black_list_member.is_displayed()


@then('Reklamlar is displayed')
def step_impl(context):
    page=VkPage(context.browser)
    page.reklamlar_is_displayed.is_displayed()

@then("Zenit web site is true")
def step_impl(context):
    time.sleep(3)
    flag = False
    if "fc-zenit" in context.browser.current_url:
        flag = True
    assert flag

@then('I am on the settings page')
def step_impl(context):
    time.sleep(3)
    flag = False
    if "settings" in context.browser.current_url:
        flag = True
    assert flag

@then('Support url is correct')
def step_impl(context):
    time.sleep(3)
    flag = False
    if "support" in context.browser.current_url:
        flag = True
    assert flag

@then('Video url is correct')
def step_impl(context):
    time.sleep(3)
    flag = False
    if "video" in context.browser.current_url:
        flag = True
    assert flag

@then('Zenit url is correct')
def step_impl(context):
    time.sleep(3)
    flag = False
    if "zenit" in context.browser.current_url:
        flag = True
    assert flag

@then('Vk Url is correct for music part')
def step_impl(context):
    flag = False
    if "audios" in context.browser.current_url:
        flag = True
    assert flag


@then('Vk url is correct for Vk connect page')
def step_impl(context):
    flag=False
    if "personal" in context.browser.current_url:
        flag=True
    assert flag

@then('Vk profile page link is displayed correctly')
def step_impl(context):
    flag=False
    if "id" in context.browser.current_url:
        flag=True
    assert flag


@then('Istanbul is displayed')
def step_impl(context):
    page=VkPage(context.browser)
    page.city_display.is_displayed()


@then('Profile username displayed in the profile page')
def step_impl(context):
    page=VkPage(context.browser)
    page.profileName.is_displayed()

@then('Sms confirmation is displayed')
def step_impl(context):
    page=VkPage(context.browser)
    page.sms_confirmation.is_displayed()


@given('I am on the Vk login page')
def step_impl(context):
    options = Options()
    options.headless = True
    context.browser = webdriver.Chrome("C://Users//Murtaza//Desktop//Courses//2021Spring//Cs439//pythonProject_proj//chromedriver_win32//chromedriver.exe",chrome_options=options)
    page=VkPage(context.browser)
    context.browser.get(page.url)
    context.browser.maximize_window()
    time.sleep(2)
