#coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep

#　测试结论：微信独立webdriver无法被appium驱动。
desired_caps = {}
desired_caps['app'] = ''
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
#desired_caps['deviceName'] = 'b8bc1bf263eb'
#desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = 'a6ac60b'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['fastReset'] = 'false'
desired_caps['fullReset'] = 'false'
desired_caps['noReset'] = 'true'

desired_caps['platformName'] = 'Android'
desired_caps['ChromeOptions.CAPABILITY'] = ["androidProcess", "com.tencent.mm:tools"]



driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#print(driver.getPageSource)
driver.implicitly_wait(10)

# driver.find_element_by_xpath("//*[@text='我']").click()
# driver.find_element_by_xpath("//*[@text='收藏']").click()
# driver.find_element_by_xpath("//*[@text='韩都衣舍']").click()

print(driver.contexts)

while True:
    #driver.swipe(300, 770, 300, 570, duration=300)
    try:
        print("Try to find your product")
        driver.find_element_by_xpath("//*[@text='我']").click()
        driver.find_element_by_xpath("//*[@text='收藏']").click()
        driver.find_element_by_xpath("//*[@text='韩都衣舍']").click()

        #driver.find_element_by_xpath("//*[@text='微信商城']").click()
        #driver.find_element_by_link_text("https://wm.maike51.com/2217646/product/productGroupPage?groupId=2846").click()
        if driver.find_element_by_link_text("https://wm.maike51.com/2217646/product/productGroupPage?groupId=2846").is_enabled():
            driver.find_element_by_link_text("https://wm.maike51.com/2217646/product/productGroupPage?groupId=2846").click()
    except:
        print("not find")
    # try:
    #     if driver.find_element_by_class_name("iconfont")[0].is_enabled():
    #         driver.find_element_by_class_name("iconfont")[0].click()
    # except:
    #     print("not find")
    # try:
    #     if driver.find_element_by_xpath("//*[@text='连衣裙']").is_enabled():
    #         driver.find_element_by_xpath("//*[@text='连衣裙']").click()
    # except:
    #     print("not find")
    # try:
    #     if driver.find_element_by_xpath("//*[@text='1130海外直邮回归'").is_enabled():
    #         driver.find_element_by_xpath("//*[@text='1130海外直邮回归'").click()
    #         sleep(1)
    #         driver.find_element_by_xpath("//*[@text='立即购买']").click()
    #         driver.find_element_by_xpath("//*[@text='30G']").click()
    #         driver.find_element_by_xpath("//*[@text='立即购买']").click()
    #         driver.find_element_by_xpath("//*[@text='去支付']").click()
    #         break
    #     #driver.execute_script('$("input[class=\'sh-button iconfont color-lv6\']").first().click()')
    #     #driver.find_element_by_class_name("sh-button iconfont color-lv6")
    #     #driver.find_element_by_xpath("//*[@id='vb-body']/div[5]/div/a/div/input").click()
    #     sleep(1)
    # except:
    #     print("not find")


print("Auto buy Test ok")
#driver.findElementByXPath("//*[@text='南街的小白楼']").click()
#driver.findElementByXPath("//*[@text='收藏']").click()
#driver.findElementByXPath("//*[contains(@text, '美团外卖')]").click()
#print(driver.getPageSource)
#print(driver.getContextHandles)
#driver.context("WEBVIEW_com.tencent.mm:toolRs")
#print(driver.getPageSource)


