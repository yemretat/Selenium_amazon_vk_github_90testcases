import time
from behave import *
from tests.acceptance.page_model.facebookbase_page import FacebookBaseLoginPage
from tests.acceptance.locators.facebookbase_page import FacebookBasePageLocators
from tests.acceptance.page_model.facebookmain_page import FacebookMainPage
from tests.acceptance.page_model.amazonlogin_page import AmazonLoginPage
use_step_matcher('re')
@Then('Invalid Gift')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    page.invalid_gift.is_displayed()

@Then('Control the Bitkiler,Tohumlar')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    print(page.bitkiler_tohumlar2.text)
    flag=False
    if "Bitkiler, Tohumlar" in page.bitkiler_tohumlar2.text:
        flag=True
    assert flag

@when("Click the Elday page")
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,500)", "")
    time.sleep(2)
    elday=page.elday_page
    elday.click()

@Then("Recycle Page Types Control")
def step_impl(context):
    page2 =AmazonLoginPage(context.browser)
    page=page2.recycle_links
    count=0
    for i in range(0,4):
        if i ==0 and page[i].text=="Elektrikli ve Elektronik Ekipman":
            count+=1
        if i==1 and page[i].text=="Piller":
            count +=1
        if i==2 and page[i].text=="Ambalajlar":
            count +=1
        if i==3 and page[i].text=="Ampuller":
            count +=1
    assert count ==4




@Then("Postal Code Message control")
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    context.browser.execute_script("window.scrollBy(0,500)", "")

    page.postal_code_message.is_displayed()


@when('Card number is "(.*)"')
def step_impl(context,content):
    page = AmazonLoginPage(context.browser)
    cardnumber=page.card_number
    if (content == cardnumber):
        return True

@when('New Name Change "(.*)"')
def step_impl(context,content):
    page = AmazonLoginPage(context.browser)
    new_name=page.new_name_update
    new_name.send_keys("")
    new_name.send_keys(content)

@when("Update Buttons Enter")
def step_impl(context):
    page =AmazonLoginPage(context.browser)
    update_buttons=page.account_update_buttons
    update_buttons[0].click()

@then('Zamani Durdur')
def step_impl(context):
    time.sleep(5)

@then('Orders "(.*)" message is displayed')
def step_impl(context,content):
    page=AmazonLoginPage(context.browser)
    message=page.ordered_product_message.text
    if content in message:
        assert True
    else:
        assert False


@then('Amazon Prime Video')
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    time.sleep(2)
    assert page.prime_video.is_displayed()

@then('Searched product "(.*)"')
def step_impl(context,content):
    page=AmazonLoginPage(context.browser)
    searched_product=page.searched_product.text
    print(searched_product)
    print(content)
    if content in searched_product:
        assert True
    else:
        assert False


@then('User name is displayed after Login')
def step_impl(context):
    page=AmazonLoginPage(context.browser)
    name=page.name_displayed
    assert name.is_displayed()

@then('There is a title shown on the page')
def step_impl(context):
    page = FacebookBaseLoginPage(context.browser)  # burada hata alıyorum !
    print(page)
    assert page.title.is_displayed()

@then("There is a Teslimat Adres button")
def step_impl(context):
    page = AmazonLoginPage(context.browser)
    assert page.title.is_displayed()


@then('There is a post by "(.*)"')
def step_impl(context, content):
    page = FacebookMainPage(context.browser)
    strongs = page.posteds
    matching_strongs = [l for l in strongs if l.text == content]
    assert len(matching_strongs) > 0

@then('Covid 19 Button here')
def step_impl(context):
    covid19Button=context.browser.find_element_by_css_selector("#u_0_h_EH")
    assert covid19Button.is_displayed()

@step('The title tag has content "(.*)"')  # step yazdığımız için her şey ile birlikte kullanabileceğiz
def step_impl(context, content):
    title_tag = context.browser.find_element(*FacebookBasePageLocators.LOGIN_LINK)
    deneme=context.browser.find_element_by_name("#mount_0_0_Q8 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.dp1hu0rb.p01isnhg > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.g5gj957u.pmt1y7k9.buofh1pr.hpfvmrgz.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.f7vcsfb0.fjf4s8hc.b6rwyo50.oyrvap6t > div > div > div:nth-child(3) > div > div.pedkr2u6.tn0ko95a.pnx7fd3z > div > div:nth-child(2) > div > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div.oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.p8dawk7l")
    assert deneme == content
