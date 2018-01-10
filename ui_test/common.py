# -*- coding: UTF-8 -*-
import random
import return_input
import time

import accout

"""通用方法"""
# 修改了splinter默认点击元素的click方法，增加延迟0.5秒

def login_console(browser):
    """登陆后台统一方法"""
    browser.visit(accout.backgroundURL)
    browser.fill('account', accout.accout)
    browser.fill('password', accout.passport)
    browser.find_by_value('登    录').click()

def choose_picture(browser,n=1):
    """
    选择图片控件统一方法
    :param n: 选择的图片数
    """
    if(n>1):
        for i in range(1,n):
            time.sleep(0.5)
            picture_group=['方图','方图二','方图三']
            browser.find_by_text(picture_group[random.randint(0,2)]).first.click()
            time.sleep(0.5)
            if random.randint(1,2) == 1:
                browser.find_by_xpath('//*[@id="pager"]/ul/li[2]/span').first.click()
            else:
                browser.find_by_xpath('//*[@id="pager"]/ul/li[3]/a').first.click()
            # 拼接成随机点击的图片排列，并使用js执行动作。
            browser.evaluate_script(return_input.random_xpath('$("li[onclick]")[', 0, 14, '].click()'))
    else:
        time.sleep(0.5)
        picture_group = ['方图', '方图二', '方图三']
        browser.find_by_text(picture_group[random.randint(0, 2)]).first.click()
        time.sleep(0.5)
        if random.randint(1, 2) == 1:
            browser.find_by_xpath('//*[@id="pager"]/ul/li[2]/span').first.click()
        else:
            browser.find_by_xpath('//*[@id="pager"]/ul/li[3]/a').first.click()
        # 拼接成随机点击的图片排列，并使用js执行动作。
        browser.evaluate_script(return_input.random_xpath('$("li[onclick]")[', 0, 14, '].click()'))
    browser.find_by_id("saveProductImage").click()
    time.sleep(0.5)


def jump_to_navi(browser,nav_title,nav_title2):
    """ 选择后台左侧导航栏，仅两级"""
    browser.find_by_text(nav_title).click()
    browser.find_by_text(nav_title2).click()
