#coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep


desired_caps = {}
desired_caps['app'] = ''
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['deviceName'] = 'b8bc1bf263eb'
desired_caps['fastReset'] = 'false'
desired_caps['fullReset'] = 'false'
desired_caps['noReset'] = 'true'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['platformName'] = 'Android'
desired_caps['ChromeOptions.CAPABILITY'] = ["androidProcess", "com.tencent.mm:tools"]



driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#print(driver.getPageSource)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@text='南街的小白楼']").click()
driver.find_element_by_xpath("//*[@text='沙箱测试']").click()

#driver.findElementByXPath("//*[@text='南街的小白楼']").click()
#driver.findElementByXPath("//*[@text='收藏']").click()
#driver.findElementByXPath("//*[contains(@text, '美团外卖')]").click()
#print(driver.getPageSource)
#print(driver.getContextHandles)
#driver.context("WEBVIEW_com.tencent.mm:toolRs")
#print(driver.getPageSource)


