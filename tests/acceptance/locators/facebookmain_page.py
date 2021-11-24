from selenium.webdriver.common.by import By


class FacebookMainPageLocators:
    TITLE = By.CLASS_NAME, 'login'
    LOGIN_LINK = By.NAME, 'login'
    SUBMIT_BUTTON = By.NAME, 'login'
    POST_FORM = By.TAG_NAME, 'form'
    STRONG_LINKS = By.TAG_NAME, 'strong'
    LIKED_POST = By.CLASS_NAME, '.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.g5gj957u.rj1gh0hx.buofh1pr.hpfvmrgz.taijpn5t' \
                                '.bp9cbjyn.owycx6da.btwxx1t3.d1544ag0.tw6a2znq.jb3vyjys.dlv3wnog.rl04r1d5.mysgfdmx' \
                                '.hddg9phg.qu8okrzs.g0qnabr5'
    LIKED_POST_babil = By.XPATH, '//*[@id="mount_0_0_RK"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[' \
                                 '2]/div/div/div[3]/div/div[4]/div/div[' \
                                 '1]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[' \
                                 '1]/div/div/div/div[1]/div[1]/div[1] '
