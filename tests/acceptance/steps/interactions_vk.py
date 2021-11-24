from tests.acceptance.page_model.vk_page import  VkPage
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

use_step_matcher('re')

@when('My problem solved button click')
def step_impl(context):
    time.sleep(1)
    page=VkPage(context.browser)
    page.myproblemsolvedbutton.click()
    time.sleep(2)
    page.size_yardimci_sevindik.is_displayed()

@when('I click the hide list question')
def step_impl(context):
    time.sleep(1)
    page=VkPage(context.browser)
    print(page.howdohidelistclick.text)
    page.howdohidelistclick.click()
    time.sleep(2)
    flag=False
    if page.hideheader.text == "How do I hide my profile from other users?":
        flag=True
    assert flag



@when('I send the input message to look sabanci')
def step_impl(context):
    page=VkPage(context.browser)
    page.sabanci_input_text.send_keys("sabanci")
    time.sleep(4)

@when('I save the button video link')
def step_impl(context):
    page=VkPage(context.browser)
    page.save_button_video_link[0].click()
    time.sleep(2)

@when('I enter the video link to input')
def step_impl(context):
    page=VkPage(context.browser)
    page.enter_web_link.send_keys("https://www.youtube.com/watch?v=_cCrsqNmPmw")
    time.sleep(4)
@when('I add the another web site')
def step_impl(context):
    page=VkPage(context.browser)
    page.add_from_another_site.click()
    time.sleep(2)


@when('Video ekle button')
def step_impl(context):
    page=VkPage(context.browser)
    page.add_video_upload[1].click()
    time.sleep(2)


@when('My video recordings click')
def step_impl(context):
    page=VkPage(context.browser)
    page.my_video_recordings.click()
    time.sleep(2)


@when('Left part click list')
def step_impl(context):
    time.sleep(2)
    page=VkPage(context.browser)
    page.video_find_left.click()
    time.sleep(2)


@when('I click the open the site')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.open_website.click()
    context.browser.switch_to_window(context.browser.window_handles[1])

@when('I click the Zenit text click')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.zenit_text_click.click()

@when('I click the abone ol zenit')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(3)
    page.abone_ol_zenit[0].click()

@when('I enter the Zenit button press')
def step_impl(context):
    page=VkPage(context.browser)
    page.topluluk_area_button.click()
    time.sleep(1)
@when('I enter the "(.*)" topluluk name')
def step_impl(context,content):
    page=VkPage(context.browser)
    page.topluluk_input_text.send_keys(content)
    time.sleep(2)
@when('I click the topluluk arama button')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(4)
    page.topluluk_arama_click[0].click()
    time.sleep(2)

@when('I click the topluluk button')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(4)
    page.click_to_topluluk.click()


@when('Share the post to the button')
def step_impl(context):
    page=VkPage(context.browser)
    page.share_post_ser.click()


@when('I click the myduvar')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(5)
    page.click_my_duvar.click()

@when('I click the share button post')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.share_post_button.click()



@when('I click the comments show')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(4)
    page.show_the_comments.click()

@when('I click the comment post button')
def step_impl(context):
    page=VkPage(context.browser)
    page.reply_button_comment.click()


@when('I enter the text "(.*)" comment post')
def step_impl(context,content):
    page=VkPage(context.browser)
    time.sleep(2)
    page.comment_to_post_write.send_keys(content)


@when('I click the comment post page')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.comment_to_post.click()

@when('I click the begenildi page')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.like_buttons_history.click()
@when('I click the svg image')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.svg_home_image.click()

@when('I like button post')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.like_button_post.click()


@when('I click the black list')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.black_list.click()
@when('I click the block button')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.engelle_button.click()

@when('I click the continue button')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.continue_click_settings.click()

@when('I click the logout button')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.logout_click.click()

@when('I click the save button in settings')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.save_button_menu_settings.click()

@when('I click the advertisements button')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(2)
    page.advertisements_click.click()

@when('I click the menu members view')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(3)
    page.menu_members.click()

@when('I click the soruyu giriniz button')
def step_impl(context):
    page=VkPage(context.browser)
    page.soruyugiriniz_text.send_keys("hide")
@when('I click the settings button')
def step_impl(context):
    time.sleep(5)
    page=VkPage(context.browser)
    page.settings_click.click()

@when('I click the help button')
def step_impl(context):
    time.sleep(5)
    page=VkPage(context.browser)
    page.help_click.click()
    time.sleep(3)

@when('I click the sag ust profile')
def step_impl(context):
    time.sleep(2)
    page=VkPage(context.browser)
    page.tosun_click_sagust.click()


@when('Top navbar click the music')
def step_impl(context):
    time.sleep(2)
    page = VkPage(context.browser)
    page.topnav_music[1].click()

@when('Date is displayed')
def step_impl(context):
    page = VkPage(context.browser)
    page.music_date_displayed.is_displayed()

@when('Music name is displayed')
def step_impl(context):
    time.sleep(2)
    page = VkPage(context.browser)
    page.music_name_displayed.is_displayed()
@when('I click the search button music')
def step_impl(context):
    time.sleep(2)
    page=VkPage(context.browser)
    page.search_button_music.click()

@when('I enter the music text "(.*)"')
def step_impl(context,content):
    time.sleep(2)
    page=VkPage(context.browser)
    page.muzik_ara_input.send_keys(content)

@when('I click the music button')
def step_impl(context):
    time.sleep(2)
    page=VkPage(context.browser)
    page.musicButton.click()

@when('I click the add friends')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(4)
    page.add_friends.click()
    time.sleep(3)

@when('I click the message gonder')
def step_impl(context):
    page=VkPage(context.browser)
    page.gonder_button.click()

@when('I click message click')
def step_impl(context):
    time.sleep(2)
    page=VkPage(context.browser)
    page.message_button.click()

@when('I enter the message box "(.*)"')
def step_impl(context,content):
    time.sleep(2)
    page=VkPage(context.browser)
    page.enter_message_text.send_keys(content)

@when('I click the Ali Tunceli list')
def step_impl(context):
    time.sleep(2)
    page = VkPage(context.browser)
    page.click_the_name_search.click()

@when('I enter the name "(.*)" to the search')
def step_impl(context,content):
    time.sleep(2)
    page = VkPage(context.browser)
    page.input_enter_search.send_keys(content)
    time.sleep(2)


@when('I click the save button')
def step_impl(context):
    page = VkPage(context.browser)
    page.save_button_change.click()
@when('I enter the "(.*)" name extra')
def step_impl(context,content):
    time.sleep(3)
    page = VkPage(context.browser)
    page.change_name.send_keys(content)


@when('I click the vk connect button')
def step_impl(context):
    time.sleep(2)
    page=VkPage(context.browser)
    page.vk_connect_enter.click()
    context.browser.switch_to_window(context.browser.window_handles[1])


@when('I click the edit button')
def step_impl(context):
    time.sleep(2)
    page=VkPage(context.browser)
    page.edit_profile_page.click()

@when('I click the delete button move to element')
def step_impl(context):
    time.sleep(2)
    page=VkPage(context.browser)
    action = ActionChains(context.browser)
    movedelement=page.delete_button_movetoElement
    time.sleep(2)
    action.move_to_element(movedelement[1]).perform()
    page.delete_post_button.click()
@when('I click the publish button')
def step_impl(context):
    page=VkPage(context.browser)
    page.publish_the_post.click()

@when('I enter the "(.*)" content to the post input')
def step_impl(context,content):
    time.sleep(1)
    page = VkPage(context.browser)
    page.post_textinput.send_keys(content)

@when('I click the login button')
def step_impl(context):
    time.sleep(1)
    page=VkPage(context.browser)
    page.loginbutton_login.click()
@when('I click the myprofile button')
def step_impl(context):
    time.sleep(3)

    page=VkPage(context.browser)
    page.myprofile_click.click()

@when('I click the continue button in sms')
def step_impl(context):
    page=VkPage(context.browser)
    page.join_send_button.click()

@when('I enter the "(.*)" phone number')
def step_impl(context,content):
    page=VkPage(context.browser)
    time.sleep(2)
    page.give_phone_number.send_keys(content)

@when('I click the continue button in register')
def step_impl(context):
    page=VkPage(context.browser)
    page.continue_click.click()

@when('I click the man gender in register')
def step_impl(context):
    page=VkPage(context.browser)
    page.man_gender_click[1].click()

@when('I click the register day "(.*)"')
def step_impl(context,content):
    page=VkPage(context.browser)
    page.day_register[int(content)].click()
@when('I click the birthday 14')
def step_impl(context):
    page=VkPage(context.browser)
    page.day_click.click()
@when('I click the birthday Mart')
def step_impl(context):
    page=VkPage(context.browser)
    time.sleep(3)
    page.month_click.click()

@when('I click the birthday 2001')
def step_impl(context):
    page=VkPage(context.browser)
    page.year_click.click()

@when('I enter the "(.*)" register surname surname field')
def step_impl(context,content):
    page=VkPage(context.browser)
    page.register_surname.send_keys(content)

@when('I enter the "(.*)" register name to name field')
def step_impl(context,content):
    page=VkPage(context.browser)
    page.register_name.send_keys(content)


@when('I give the "(.*)" phone to the email')
def step_impl(context,content):
    page=VkPage(context.browser)
    page.get_email.send_keys(content)

@when('I give the "(.*)" password to the password field')
def step_impl(context,content):
    page=VkPage(context.browser)
    page.get_password.send_keys(content)

@when('I click the sign in button')
def step_impl(context):
    page=VkPage(context.browser)
    page.button_click.click()