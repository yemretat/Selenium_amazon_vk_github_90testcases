import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.acceptance.page_model.facebookbase_page import FacebookBaseLoginPage
from tests.acceptance.page_model.facebookmain_page import FacebookMainPage
from tests.acceptance.page_model.amazonlogin_page import AmazonLoginPage

use_step_matcher('re')  # navigationfeaturesdaki scenariodan bilgi alma

@then('I am on the Elday web page')
def step_impl(context):
    flag=False
    if "elday.org" in context.browser.current_url:
        flag=True
    assert flag

@when("Time")
def step_impl(context):
    time.sleep(15)

@then('I am on the app store')
def step_impl(context):
    flag=False
    time.sleep(2)
    if "https://apps.apple.com/" in context.browser.current_url:
        flag=True
        print("doğru")
    print(context.browser.current_url)
    assert flag


@then('I am on the app page')
def step_impl(context):
    flag=False
    time.sleep(3)
    if "mobapp" in context.browser.current_url:
        flag=True
        print("doğru")
    print(context.browser.current_url)
    assert flag


@then('I am on the page 2')
def step_impl(context):
    flag=False
    time.sleep(3)
    if "pg_2" in context.browser.current_url:
        flag=True
        print("doğru")
    print(context.browser.current_url)
    assert flag


@then('I am on the SignIn page')
def step_impl(context):
    flag=False
    time.sleep(3)
    if "signin" in context.browser.current_url:
        flag=True
        print("doğru")
    print(context.browser.current_url)
    assert flag

@then('I am on the computer page')
def step_impl(context):
    flag = False
    time.sleep(3)
    if "bilgisayar" in context.browser.current_url:
        flag = True
        print("doğru")
    print(context.browser.current_url)
    assert flag


@then('I am the amazon jobs page')
def step_impl(context):
    flag = False
    time.sleep(3)
    if "signin" == context.browser.current_url:
        flag = True
        print("doğru")
    print(context.browser.current_url)
    assert flag
@then('I am on the Amazon Services')
def step_impl(context):
    flag=False
    if "services" in context.browser.current_url:
        flag=True
    assert flag
@then('I am on the help Services')
def step_impl(context):
    flag=False
    if "help/customer" in context.browser.current_url:
        flag=True
    assert flag

@then('I am on the Youtube Channel')
def step_impl(context):
    flag=False
    context.browser.switch_to_window(context.browser.window_handles[1])
    if "youtube" in context.browser.current_url:
        flag=True
    assert flag
@then('I am on the contact us page')
def step_impl(context):
    flag=False
    if "contact-us" in context.browser.current_url:
        flag=True
    assert flag

@then('I am on the Amazon Benefits Page')
def step_impl(context):
    assert "https://www.amazon.jobs/en/benefits" == context.browser.current_url

@then('I am on the Amazon Jobs Page')
def step_impl(context):
    assert "https://www.amazon.jobs/en/" == context.browser.current_url

@then('I am on the Amazon cok satanlar page')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    assert context.browser.current_url == page.urlCokSatanlar

@then ('I am on the gold box page')
def step_impl(context):
    flag=False
    if "goldbox" in context.browser.current_url:
        flag = True
        print("Gold box True")
    assert flag
@then('I am on the Amazon Prime Gaming')
def step_impl(context):
    flag=False
    if "gaming" in context.browser.current_url:
        flag=True
    assert flag


@then('I am on the Amazon Prime Page')
def step_impl(context):
    flag =False
    if "prime" in context.browser.current_url:
        flag=True
        print("doğru")
    assert flag

@then('I am on the Amazon entrance page')
def step_impl(context):
    assert context.browser.current_url== "https://www.amazon.com.tr/" or context.browser.current_url=="https://www.amazon.com.tr/?ref_=nav_signin&"

@given('I am on the Amazon entrance page')
def step_impl(context):
    options = Options()
    options.headless = True
    context.browser = webdriver.Chrome(
        "C://Users//Murtaza//Desktop//Courses//2021Spring//Cs439//pythonProject_proj//chromedriver_win32//chromedriver.exe",chrome_options=options)
    page = AmazonLoginPage(context.browser)
    context.browser.get(page.url)
    context.browser.maximize_window()
    time.sleep(1)


@given('I am on the login page')
def step_impl(context):
    context.browser = webdriver.Chrome(
        "C://Users//Murtaza//Desktop//Courses//2021Spring//Cs439//pythonProject_proj//chromedriver_win32//chromedriver.exe")
    page = FacebookBaseLoginPage(context.browser)
    context.browser.get(page.url)


@given('I am on the main page')
def step_impl(context):
    context.browser = webdriver.Chrome(
        "C://Users//Murtaza//Desktop//Courses//2021Spring//Cs439//pythonProject_proj//chromedriver_win32//chromedriver.exe")
    page = FacebookMainPage(context.browser)
    context.browser.get(page.url)
