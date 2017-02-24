# -*- coding: UTF-8 -*-
from splinter import Browser
import time, sys, return_input
import random, unittest
# 修改了splinter默认点击元素的click方法，增加延迟0.5秒

def login_console():
    """登陆后台统一方法"""
    accout = "18781901199"
    passport = "miang521"
    backgroundURL = "http://shop.aiyaohong.com"
    browser.visit(backgroundURL)
    browser.fill('account', accout)
    browser.fill('password', passport)
    browser.find_by_value('登    录').click()

def choose_picture(n=1):
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
            browser.evaluate_script(return_input.random_xpath('$("li[onclick]")[',0,14,'].click()'))
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


def jump_to_navi(nav_title,nav_title2):
    """ 选择后台左侧导航栏，仅两级"""
    browser.find_by_text(nav_title).click()
    browser.find_by_text(nav_title2).click()

class pub_product:
    # 变量
    productName = return_input.productName
    shortDes = return_input.shortDes
    productCode = return_input.random_special_charactor()+'MAIKEt'
    share_title = return_input.share_title
    share_content = return_input.share_content
    def jump_to_edit(self,browser):
        browser.find_by_text('发布商品').click()
        browser.find_by_id(return_input.random_xpath('item_', 1, 5)).first.click()
        browser.find_by_text('下一步').click()

    def fill_product_info(self,browser):
        # 商品基本信息
        browser.find_by_id('productName').fill(self.productName)
        browser.find_by_id('shortDes').fill(self.shortDes)
        browser.find_by_id('productCode').fill(self.productCode)

    def fill_sku_name(self,browser):
        # 商品规格
        browser.find_by_text('添加规格项目').click()
        browser.find_by_text('添加规格').click()
        browser.find_by_xpath('//*[@id="addSkuWindow"]/div/div/fieldset[1]/div/div/span/span/input').fill('尺码')
        browser.find_by_xpath('//*[@id="toAddSku"]').click()
        time.sleep(0.5)
        browser.find_by_xpath('//*[@id="addSpecV_0"]').click()
        time.sleep(0.5)
        browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').click()
        browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').fill('L')
        time.sleep(0.5)
        browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[2]/button').click()
        time.sleep(0.5)
        browser.find_by_xpath('//*[@id="addSpecV_0"]/a').click()
        time.sleep(0.5)
        browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input'). \
            fill(return_input.product_sku)
        browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[2]/button').click()
        browser.evaluate_script('$(".mk-product-body").scrollTop(1000)')

    def fill_sku_price(self,browser):
        # 规格挂牌价格
        browser.evaluate_script(
            'document.getElementById("batch_quto").style="display: inline-block; visibility: visible;"')
        browser.find_by_id('batch_quto').fill(return_input.sku_quto)
        browser.evaluate_script('document.getElementById("batch_quto").style="display: none; visibility: visible;"')
        time.sleep(0.5)
        browser.find_by_xpath('//*[@id="quto_yes"]').click()

        browser.evaluate_script(
            'document.getElementById("batch_sale").style="display: inline-block; visibility: visible;"')
        browser.find_by_id('batch_sale').fill(return_input.sku_price)
        browser.evaluate_script('document.getElementById("batch_sale").style="display: none; visibility: visible;"')
        browser.find_by_id("sale_yes").click()

        browser.evaluate_script(
            'document.getElementById("batch_inventory").style="display: inline-block; visibility: visible;"')
        browser.find_by_id('batch_inventory').fill(return_input.p_inventory)
        browser.evaluate_script(
            'document.getElementById("batch_inventory").style="display: none; visibility: visible;"')
        browser.find_by_id("inventory_yes").click()

        browser.find_by_id("batch_skuCode").fill(return_input.skuCode)
        browser.find_by_id("code_yes").click()
        time.sleep(0.5)


    def set_sku_picture(self,browser):
        # sku 图片设置 //*[@id="skuImgTable"]/tbody/tr/td/div[1]/button
        browser.evaluate_script('$("#chkSkuImg").click()')
        browser.find_by_xpath('//*[@id="skuImgTable"]/tbody/tr/td/div[1]/button').click()
        choose_picture(1)
        browser.find_by_xpath('//*[@id="skuImgTable"]/tbody/tr/td/div[2]/button').click()
        choose_picture(1)


    def choose_SoldQty_Inventory(self,browser):
        """勾选：商城是否显示销量和购买记录   商城是否显示库存"""
        browser.evaluate_script('$("#displaySoldQty").click()')
        browser.evaluate_script('$("#displayInventory").click()')
        browser.evaluate_script('$(".mk-product-body").scrollTop(2000)')


    def set_share(self,browser):
        """设置分享内容"""
        browser.evaluate_script('window.scrollTo(0,0)')
        time.sleep(0.5)
        browser.find_by_xpath('//*[@id="productInfo"]/div[5]/div[2]/div/div[1]/div/div/button').click()
        time.sleep(0.5)
        choose_picture()
        browser.find_by_id('shareTitle').fill(self.share_title)
        browser.find_by_id('shareContent').fill(self.share_content)


    def set_product_picuture(self,browser):
        """配置图片"""
        # 方图
        browser.find_by_xpath('//*[@id="productInfo"]/div[6]/div[2]/div/div[1]/div/button').click()
        choose_picture(4)
        # 宽图
        browser.find_by_xpath('//*[@id="productInfo"]/div[6]/div[2]/div/div[3]/div/button').click()
        time.sleep(0.5)
        browser.find_by_text('长图一服装').click()
        time.sleep(0.5)
        browser.evaluate_script(return_input.random_xpath('$("li[onclick]")[',0,14,'].click()'))
        browser.find_by_xpath('//*[@id="saveProductImage"]').click()
        time.sleep(0.5)
        browser.evaluate_script('$(".mk-product-body").scrollTop(5000)')


    def set_shipping_free(self,browser):
        # 运费设置
        browser.find_by_xpath("(//input[@name='shippingType'])[2]").click()
        browser.find_by_text('请选择').click()
        time.sleep(0.5)
        browser.find_by_text('四川免运').click()
        browser.evaluate_script('$(".mk-product-body").scrollTop(6000)')

    def set_logisticsWeight(self,browser):
        # 物流重量，使用jquery填充和单击输入框
        browser.evaluate_script('$("input[id^=\'logisticsWeight\']").first().val("500")')
        browser.evaluate_script('$("input[class=\'k-formatted-value noEdit k-input\']").first().click()')
        browser.evaluate_script('$("input[id^=\'logisticsWeight\'").last().val("1500")')
        browser.evaluate_script('$("input[class=\'k-formatted-value noEdit k-input\']").last().click()')

    def set_sale_type(self,browser):
        browser.find_by_name("saleType").click()
        browser.find_by_xpath("(//input[@name='stockReduceType'])[2]").click()
        # browser.find_by_id("toOn").click()
        time.sleep(0.5)
        # browser.find_by_xpath('/html/body/div[1]/div/div[3]/a').click()

# runTest

browser = Browser('chrome', )
browser.driver.set_window_size(1600, 1000)
login_console()
jump_to_navi('商品管理', '商品仓库')
pub = pub_product()
pub.jump_to_edit(browser)
pub.fill_product_info(browser)
pub.fill_sku_name(browser)
pub.fill_sku_price(browser)
pub.set_sku_picture(browser)
pub.choose_SoldQty_Inventory(browser)
pub.set_share(browser)
pub.set_product_picuture(browser)
pub.set_shipping_free(browser)
pub.set_sale_type(browser)




