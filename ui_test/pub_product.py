# -*- coding: UTF-8 -*-

from ui_test.common import *

# 修改了splinter默认点击元素的click方法，增加延迟0.5秒
# 变量
productName = return_input.productName
shortDes = return_input.shortDes
productCode = return_input.random_special_charactor() + 'MAIKEt'
share_title = return_input.share_title
share_content = return_input.share_content
def jump_to_edit(browser):
    browser.find_by_text('发布商品').click()
    browser.find_by_id(return_input.random_xpath('item_', 1, 5)).first.click()
    browser.find_by_text('下一步').click()

def fill_product_info(browser):
    # 商品基本信息
    browser.find_by_id('productName').fill(productName)
    browser.find_by_id('shortDes').fill(shortDes)
    browser.find_by_id('productCode').fill(productCode)

def fill_sku_name(browser):
    # 商品规格
    browser.find_by_text('添加规格项目').click()
    browser.find_by_text('添加规格').click()
    browser.find_by_xpath('//*[@id="addSkuWindow"]/div/div/fieldset[1]/div/div/span/span/input').fill('尺码')
    browser.find_by_xpath('//*[@id="toAddSku"]').click()
    time.sleep(0.5)
    browser.find_by_xpath('//*[@id="addSpecV_0"]').click()
    time.sleep(1)
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

def fill_sku_price(browser):
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


def set_sku_picture(browser):
    # sku 图片设置 //*[@id="skuImgTable"]/tbody/tr/td/div[1]/button
    browser.evaluate_script('$("#chkSkuImg").click()')
    browser.find_by_xpath('//*[@id="skuImgTable"]/tbody/tr/td/div[1]/button').click()
    choose_picture(browser, 1)
    browser.find_by_xpath('//*[@id="skuImgTable"]/tbody/tr/td/div[2]/button').click()
    choose_picture(browser, 1)


def choose_SoldQty_Inventory(browser):
    """勾选：商城是否显示销量和购买记录   商城是否显示库存"""
    browser.evaluate_script('$("#displaySoldQty").click()')
    browser.evaluate_script('$("#displayInventory").click()')
    browser.evaluate_script('$(".mk-product-body").scrollTop(2000)')


def set_share(browser):
    """设置分享内容"""
    browser.evaluate_script('window.scrollTo(0,0)')
    time.sleep(0.5)
    browser.find_by_xpath('//*[@id="productInfo"]/div[5]/div[2]/div/div[1]/div/div/button').click()
    time.sleep(0.5)
    choose_picture(browser)
    browser.find_by_id('shareTitle').fill(share_title)
    browser.find_by_id('shareContent').fill(share_content)


def set_product_picuture(browser):
    """配置图片"""
    # 方图
    browser.find_by_xpath('//*[@id="productInfo"]/div[6]/div[2]/div/div[1]/div/button').click()
    choose_picture(browser, 4)
    # 宽图
    browser.find_by_xpath('//*[@id="productInfo"]/div[6]/div[2]/div/div[3]/div/button').click()
    time.sleep(0.5)
    browser.find_by_text('长图一服装').click()
    time.sleep(0.5)
    browser.evaluate_script(return_input.random_xpath('$("li[onclick]")[', 0, 14, '].click()'))
    browser.find_by_xpath('//*[@id="saveProductImage"]').click()
    time.sleep(0.5)
    browser.evaluate_script('$(".mk-product-body").scrollTop(5000)')


def set_shipping_free(browser):
    # 运费设置
    browser.find_by_xpath("(//input[@name='shippingType'])[2]").click()
    browser.find_by_text('请选择').click()
    time.sleep(0.5)
    browser.find_by_text('四川免运').click()
    browser.evaluate_script('$(".mk-product-body").scrollTop(6000)')

def set_logisticsWeight(browser):
    # 物流重量，使用jquery填充和单击输入框
    browser.evaluate_script('$("input[id^=\'logisticsWeight\']").first().val("500")')
    browser.evaluate_script('$("input[class=\'k-formatted-value noEdit k-input\']").first().click()')
    browser.evaluate_script('$("input[id^=\'logisticsWeight\'").last().val("1500")')
    browser.evaluate_script('$("input[class=\'k-formatted-value noEdit k-input\']").last().click()')
    return 1

def set_sale_type(browser):
    browser.find_by_name("saleType").click()
    browser.find_by_xpath("(//input[@name='stockReduceType'])[2]").click()
    browser.find_by_id("toOn").click()
    time.sleep(0.5)
    browser.find_by_xpath('/html/body/div[1]/div/div[3]/a').click()
    return 0

# runTest

class Test_pub_product(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):



    # @classmethod
    # def tearDownClass(cls):
    #     # browser.windows[0].close()

    def test_pub_product(self):
        browser = Browser('chrome', )
        browser.driver.set_window_size(1600, 1000)
        login_console(browser)
        jump_to_navi(browser, '商品管理', '商品仓库')
        jump_to_edit(browser)
        fill_product_info(browser)
        fill_sku_name(browser)
        fill_sku_price(browser)
        set_sku_picture(browser)
        choose_SoldQty_Inventory(browser)
        set_share(browser)
        set_product_picuture(browser)
        set_shipping_free(browser)
        self.assertEqual(0, set_sale_type(browser))




