# -*- coding: utf-8 -*-
from splinter import Browser
import datetime, time


browser = Browser('chrome', )
browser.driver.set_window_size(1600, 1000)
browser.visit("https://open.weixin.qq.com/")
browser.find_by_id("loginBarBt").click()
browser.find_by_name("account").fill(u"siyin@maike51.com")
browser.find_by_name("passwd").fill(u"xxx")
browser.find_by_text("登录")[2].click()

browser.find_by_xpath("//*[@data-param='appid=wxfb1fb56deb2664a8']").click()
time.sleep(2)
browser.windows.current = browser.windows[1]
n = 200
while True:
    browser.evaluate_script('window.scrollTo(0,%d)'%n)
    if browser.is_element_present_by_id('js_fastmodify_ip'):
        break


browser.find_by_id('js_fastmodify_ip').first.click()
browser.find_by_xpath("/html/body/div[6]/div/div[2]/textarea").fill(u"118.116.127.7")
browser.find_by_text('确定').click()
time.sleep(2)
browser.quit()