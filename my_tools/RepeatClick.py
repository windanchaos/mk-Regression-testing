# -*- coding: utf-8 -*-
"""重复点击后台，监控延迟出现时间"""
from splinter import Browser
import datetime, time
import accout

loop1 = 0.0
loop2 = 0.0

print("监控开始时间：",datetime.datetime.now())
while 1:
    browser = Browser('chrome', )
    browser.driver.set_window_size(1600, 1000)
    browser.visit(accout.backgroundURL)
    browser.find_by_text('个人店主登录')
    browser.fill('account', accout.account)
    browser.fill('password', accout.passport)
    browser.find_by_value('登    录').click()



    titles = ['店铺收入', '资金明细', '提现', '对账单']
    urls = ['settle', 'settle/acctDetail', 'settle/withdrawApply', 'statement/accountStatementPage']
    titles2 = ['卖盟计划', '商品仓库', '商品分组', '物流设置']
    urls2 = ['supplierPlan/setRecommendProductsPage', 'product/productManage', 'productGroups/', 'templates/']
    titles3 = ['账户总览', '订单管理']
    urls3 = ['yunAcct/acctIndex', 'yunAcct/acctDetailIndex', 'yunAcct/yunOrderIndex', 'yunAcct/acctDetailIndex']


    # 登录后点600次然后再登录
    for n in range(0,600):
        browser.find_by_text('店铺资产').click()
        for i in range(0,4):
            loop1+=1.0
            starttime = datetime.datetime.now()
            browser.find_by_text(titles[i]).first.click()
            if browser.status_code == 200 or browser.url == (accout.backgroundURL+urls[i]):
                endtime = datetime.datetime.now()
                if (endtime-starttime).seconds > 4:
                    print("点击==店铺资产==的:",titles[i])
                    print("点击资产菜单相差:",(endtime-starttime).seconds,'s')
                    print("产生时间:",endtime)
                    print("循环次数:",loop1)



        browser.find_by_text('商品管理').click()
        for i in range(0, 4):
            loop2+=1.0
            starttime = datetime.datetime.now()
            browser.find_by_text(titles2[i]).first.click()
            if browser.status_code == 200 or browser.url == (accout.backgroundURL+urls2[i]):
                # print("点了:", loop2)
                endtime = datetime.datetime.now()
                if (endtime-starttime).seconds > 4:
                    print("点击==商品管理==的:", titles2[i])
                    print("点击资产菜单相差:",(endtime-starttime).seconds,'s')
                    print("产生时间:",endtime)
                    print("循环次数:",loop2)

    browser.driver.close()
        #
        # browser.find_by_text('费用中心').click()
        # time.sleep(0.5)
        # for i in range(0, 2):
        #     starttime = datetime.datetime.now()
        #     browser.find_by_text(titles3[i]).first.click()
        #     if browser.status_code == 200 or browser.url == (backgroundURL+urls3[i]):
        #         endtime = datetime.datetime.now()
        #         if (endtime-starttime).seconds > 3:
        #             print("点击资产菜单相差:")
        #             print((endtime-starttime).seconds)
        #             print("产生时间:")
        #             print(endtime)
