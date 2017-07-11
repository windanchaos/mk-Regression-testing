#coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep


desired_caps = {}
desired_caps['app'] = ''
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['deviceName'] = '760BBKT22W8B'
desired_caps['fastReset'] = 'false'
desired_caps['fullReset'] = 'false'
desired_caps['noReset'] = 'true'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['platformName'] = 'Android'
desired_caps['ChromeOptions.CAPABILITY'] = ["androidProcess", "com.tencent.mm:tools"]



driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#print(driver.getPageSource)
driver.findElementByXPath("//*[@text='我']").click()
driver.findElementByXPath("//*[@text='收藏']").click()
driver.findElementByXPath("//*[contains(@text, '美团外卖')]").click()
#print(driver.getPageSource)
#print(driver.getContextHandles)
driver.context("WEBVIEW_com.tencent.mm:tools")
#print(driver.getPageSource)


