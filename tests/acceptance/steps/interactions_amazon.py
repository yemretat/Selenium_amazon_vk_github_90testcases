from behave import *
import time
from selenium.webdriver.support.ui import Select
addedProduct = ""

from tests.acceptance.page_model.facebookbase_page import FacebookBaseLoginPage
from tests.acceptance.page_model.facebookmain_page import FacebookMainPage
from tests.acceptance.page_model.amazonlogin_page import AmazonLoginPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

use_step_matcher('re')


@when("Gift Code button click")
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    page.gift_code_button.click()


@when('Gift Code "(.*)" Upload')
def step_impl(context,content):
    page=AmazonLoginPage(context.browser)
    page.gift_code_upload.send_keys(content)


@when("Gift Card Upload")
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    page.gift_card_upload[1].click()

@when('Click the Bitkiler,Tohumlar ve Soganlar')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    page.bitkiler_tohumlar.click()


@when('Click the Garden')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    page.go_to_garden.click()
    time.sleep(2)

@when("Click the navbar all")
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    page.navbar_all.click()
    time.sleep(2)


@when("Click the profile names")
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,2000)", "")
    time.sleep(2)
    context.browser.execute_script("window.scrollBy(0,500)", "")

    profile_name=page.profile_names[0]
    time.sleep(2)
    name_user=profile_name.text

    profile_name.click()
    print(name_user)
    time.sleep(2)
    real_name_user=page.real_comment_user.text
    print(real_name_user)
    flag=False
    if name_user == real_name_user:
        flag=True
    assert flag




@when('Save product for later to the Card and control')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    time.sleep(3)
    page.card_product_names.is_displayed()
    time.sleep(2)
    print("1")
    page.saveforlater[0].click()
    print("2")
    time.sleep(3)
    context.browser.execute_script("window.scrollBy(0,200)", "")
    page.saved_for_later_products.is_displayed()



@when('Delete the card')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    time.sleep(2)
    page.cart_delete[0].click()


@when('Click the card image')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    page.cart_image.click()


@when('Card delete button')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    page.card_delete.click()

@when('I select the search drop down')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    time.sleep(1)
    select=Select(page.search_drop_down)
    select.select_by_index(9)

@when('I select the quantity')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    time.sleep(1)
    time.sleep(3)
    select=Select(page.selectQuantity)
    select.select_by_value("2")

@when('View History Titles same with previous vivewed item')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    time.sleep(1)
    titles=page.view_history_titles[0]
    print("added product is {}".format(addedProduct))
    print("title product is {}".format(titles.text))
    flag=False
    if titles.text in addedProduct:
        flag=True
    assert flag


@when('Click the view history')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,3500)", "")
    time.sleep(3)
    context.browser.execute_script("window.scrollBy(0,500)", "")
    time.sleep(3)

    page.view_history.click()


@when('Go to the amazon base page again')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.amazon_logo.click()


@when('I click the accept_cookies')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.accept_cookies.click()


@when('I click the recycle href')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,3200)", "")
 #   time.sleep(2)
    page.recycle_A.click()


@when('I enter the postal code control')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.postal_code_button.click()


@when('I enter the "(.*)" postal code')
def step_impl(context, content):
    page = AmazonLoginPage(context.browser)
    page.enter_postalcode.send_keys(content)


@when('Go to the free shipping')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,1700)", "")
    page.free_shipping.click()


@when('Make a comment')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,2200)", "")
    time.sleep(3)
    page.make_comment.click()


@when('I make a list')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    time.sleep(2)
    page.make_a_list_button.click()


@when('I select the Account and Lists to Make a list')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    action = ActionChains(context.browser)
    action.move_to_element(page.register_select).perform()
    page.make_a_list.click()


@when("Complete the shopping")
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.continue_to_marketing.click()


@when("Click the Card Image")
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.press_to_card.click()


@when("I add the products")
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    time.sleep(4)
    page.products_to_buy[0].click()
    addedProduct = page.added_product_title.text
    print("Added product 1 is {}".format(addedProduct))


@when('Login and Security open')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.login_security.click()
    time.sleep(1)


@when('I select the Account and Lists to my Account')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    action = ActionChains(context.browser)
    action.move_to_element(page.register_select).perform()
    page.myaccount_hidden.click()


@when('I select the Account and Lists to Siparislerim')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    action = ActionChains(context.browser)
    action.move_to_element(page.register_select).perform()
    page.orders_hidden.click()


@when('Go to the min value')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    min_value = page.git_min_value
    min_value.click()
    time.sleep(2)
    print("Go to the min value")


@then('The min value is "(.*)"')
def step_impl(context, content):
    page = AmazonLoginPage(context.browser)
    min_values = page.get_the_prices
    flag = True
    content = float(content) / 1000
    print("Content is {}".format(content))
    for i in range(0, 15):
        #        print(min_values[i].text)
        if float(min_values[i].text) < content:
            flag = False
    assert flag


@when('I press the min value "(.*)"')
def step_impl(context, content):
    page = AmazonLoginPage(context.browser)
    min_value = page.enter_min_value_input
    min_value.send_keys(content)
    time.sleep(3)


@when('I press the search button')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    search_submit = page.search_submit
    search_submit.click()


@when('I logout from the hidden')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    action = ActionChains(context.browser)
    action.move_to_element(page.register_select).perform()
    page.logout_hidden.click()


@when('I select the Account and Lists to Login')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    action = ActionChains(context.browser)
    action.move_to_element(page.register_select).perform()
    page.giris_yap_hidden.click()


@when('I select the Account and Lists to Register')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    action = ActionChains(context.browser)
    action.move_to_element(page.register_select).perform()
    time.sleep(2)
    page.hidden_uye_olun.click()


@when('I click the Address Content')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    address_content = page.addressContent
    address_content.click()


@when('I click the App Store image')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    amazon_app = page.appstore
    amazon_app.click()
    print("Window {}".format(context.browser.window_handles))
    context.browser.switch_to_window(context.browser.window_handles[1])


@when('I click the Teslimat Adresini Secin')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    address = page.address_Choose
    address.click()
    time.sleep(1)


@when('I click the complete the shopping')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    shopping = page.complete_Shopping
    shopping.click()


@when('I click the Card Button')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    add_toCard = page.sepeteEkle
    add_toCard.click()


@when('I click the Amazon App')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,3800)", "")
    amazon_app = page.amazon_app
    amazon_app.click()


@when('I click the next button')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,3400)", "")

    pg_2 = page.page_passing[0]
    pg_2.click()


@when('I click the 500 tl and above')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,700)", "")
    fivehundred = page.fivehundred_above
    fivehundred.click()


@when('I click the prime video')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,1300)", "")
    prime_Video = page.prime_video
    prime_Video.click()


@when('I click the firsatlari yakala button')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,1600)", "")
    but = page.firsatlari_yakala
    but.click()


@when('I click the Bilgisayar NavBar')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    computer = page.computer_navbar
    computer.click()


@when('I click the no thanks')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    time.sleep(1)
    page.dont_want_Amazon_prime.click()
    time.sleep(1)


@when('I click the communication_A')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,3800)", "")
    time.sleep(1)
    page.communication_href.click()


@when('I click the reach to us')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,800)", "")
    time.sleep(1)
    page.reach_us_button.click()


@when('I click the Kariyer_A')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,3800)", "")
    time.sleep(1)
    page.kariyer_href.click()


@when('I click the Amazon_Sales_A')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,3800)", "")
    time.sleep(1)
    page.amazon_sales_href.click    ()


@when('I click the YoutubePOPUP')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.youtube_popup[1].click()


@when('I click the benefits')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    time.sleep(1)
    page.benefits_href.click()


@when('I click 30 day free button to start')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    # context.browser.execute_script("window.scrollBy(0,1300)", "")
    time.sleep(2)
    context.browser.switch_to_window(context.browser.window_handles[1])

    clickw = page.thirtday_free_try_tostart

    clickw.click()
    time.sleep(2)


@when('I click 30 day free button')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,2600)", "")
    time.sleep(3)
    page.thirtday_free_try[2].click()


@when('I move to the account element')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    ActionChains(context.browser).move_to_element(page.account_movetoelement)
    time.sleep(2)


@then('I click the checkbox')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    time.sleep(2)
    page.checkbox.click()
    time.sleep(1)


@when('I press the price gaming')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,500)", "")

    time.sleep(1)
    page.primegaming_div.click()
    time.sleep(1)


@when('I press the Price Gaming Kesfet')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    time.sleep(1)
    page.primegaming_start.click()
    time.sleep(1)


@when('I press the 30 gun ucretsiz deneme')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    time.sleep(1)
    context.browser.execute_script("window.scrollBy(0,1000  )", "")

    page.textli_A.click()
    time.sleep(1)


@when('I press the "(.*)" name country')
def step_impl(context, content):
    page = AmazonLoginPage(context.browser)
    select = page.selectCountry(content)
    drop = Select(select)
    drop.select_by_index(1)
    time.sleep(3)
    select.select_by_value("TC")


@when('I press the "(.*)" idli button')
def step_impl(context, content):
    page = AmazonLoginPage(context.browser)
    page.idliButton(content).click()


@when('I press the buy now button Satin Al')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.buyNowButton.click()
    time.sleep(1)


@when('I press the Xiaomi Satin Al')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.tuvaletKagidiSatinAl.click()
    time.sleep(1)


@when('I press the Cok Satanlar Button')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    page.cok_satan_button.click()
    time.sleep(1)


@when('I enter the "(.*)" "(.*)" idli text')
def step_impl(context, content, id):
    page = AmazonLoginPage(context.browser)
    page.idliText(id).send_keys(content)
    time.sleep(1)


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, name):
    page = AmazonLoginPage(context.browser)
    page.enterFormfield(name).send_keys(content)


@when('I enter the "(.*)" in the search bar field')
def step_impl(context, content):
    page = AmazonLoginPage(context.browser)
    page.searchBar.send_keys(content)


@when('I press the submit button')
def step_impl(context):
    page = FacebookBaseLoginPage(context.browser)
    page.submit_button.click()


# @when('I enter "(.*)" in the "(.*)" field')
# def step_impl(context, content, field_name):
#    page = FacebookBaseLoginPage(context.browser)
#    page.form_field(field_name).send_keys(content)


@when('I press the post section')
def step_impl(context):
    page = FacebookBaseLoginPage(context.browser)
    page.submit_button.click()


@then('I press the like button')
def step_impl(context):
    likeBtn = context.browser.find_element_by_css_selector(
        "#mount_0_0_Q8 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.dp1hu0rb.p01isnhg > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.g5gj957u.pmt1y7k9.buofh1pr.hpfvmrgz.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.f7vcsfb0.fjf4s8hc.b6rwyo50.oyrvap6t > div > div > div:nth-child(3) > div > div.pedkr2u6.tn0ko95a.pnx7fd3z > div > div:nth-child(2) > div > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div.oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.p8dawk7l")

    likeBtn.liked_button.click()
