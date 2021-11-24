from tests.acceptance.page_model.vk_page import  VkPage
import time
from behave import *

use_step_matcher('re')



@then('Block button notification is correct')
def step_impl(context):
   time.sleep(2)
   page=VkPage(context.browser)
   page.engelle_button_notificaton.is_displayed()

@then('Talepname is visible')
def step_impl(context):
   time.sleep(5)
   page=VkPage(context.browser)
   page.talepname_sent.is_displayed()

@then('Name is displayed in profile page')
def step_impl(context):
   time.sleep(3)
   page=VkPage(context.browser)
   page.profile_name_true.is_displayed()

@then('Content surname is displayed')
def step_impl(context):
   page=VkPage(context.browser)
   page.edit_surname_displayed.is_displayed()

@then('Content name is displayed')
def step_impl(context):
   time.sleep(2)
   page=VkPage(context.browser)
   page.edit_name_displayed.is_displayed()

@when('Profile username displayed in the profile page')
def step_impl(context):
   time.sleep(3)
   page=VkPage(context.browser)
   page.profileName.is_displayed()
