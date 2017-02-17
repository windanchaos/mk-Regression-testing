# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PubPro(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://passpt.aiyaohong.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_pub_pro(self):
        driver = self.driver
        driver.set_window_size(1600, 1000)
        driver.get(self.base_url + "/?refer=shop")
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("18781901199")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("miang521")
        driver.find_element_by_css_selector("div.btns-box > #login-button").click()
        driver.find_element_by_css_selector("div.nav-title").click()
        driver.find_element_by_xpath("//li[2]/a/div").click()
        driver.find_element_by_id("addProduct").click()
        driver.find_element_by_id("item_2").click()
        driver.find_element_by_id("next").click()
        driver.find_element_by_id("productName").clear()
        driver.find_element_by_id("productName").send_keys(u"自动测试商品")
        driver.find_element_by_id("shortDes").clear()
        driver.find_element_by_id("shortDes").send_keys(u"自动测试商品")
        # 添加第一个规格
        driver.find_element_by_id("addSpec").click()
        driver.find_element_by_xpath('//*[@id="productInfo"]/div[4]/div[2]/div[1]/div[1]/div[1]/button').click()
        # driver.find_element_by_xpath("//button[@onclick='openSelSpecWindow(this);']").click()
        driver.find_element_by_xpath('//*[@id="addSkuWindow"]/div/div/fieldset[1]/div/div/span/span/input').\
            send_keys('净含量')
        # driver.find_element_by_xpath("//div[@id='addSkuWindow']/div/div/fieldset/div/div/span/span/span/span").click()
        driver.find_element_by_id("toAddSku").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"+添加").click()
        # find_element_by_xpath("//div[@id='skuValueWindow']/div/div/fieldset/div/div/span/span/span/span").click()
        driver.find_element_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').\
            send_keys('1L')
        driver.find_element_by_xpath("//button[@onclick='addSkuValue();']").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"+添加").click()
        # find_element_by_xpath("//div[@id='skuValueWindow']/div/div/fieldset/div/div/span/span/span/span").click()
        driver.find_element_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').\
            send_keys('2L')
        driver.find_element_by_xpath("//button[@onclick='addSkuValue();']").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"+添加").click()
        driver.find_element_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').\
            send_keys('3L')
        driver.find_element_by_xpath("//button[@onclick='addSkuValue();']").click()
        time.sleep(1)
        # driver.find_element_by_id("batch_quto").clear()
        driver.find_element_by_id("batch_quto").send_keys("120")
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()

        # driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="skuShow"]/div[1]/div/div[2]/div[1]/span[2]/span/input[1]').clear()
        # driver.find_element_by_xpath('//*[@id="skuShow"]/div[1]/div/div[2]/div[1]/span[2]/span/input[1]').\
        #     send_keys('120')

        driver.find_element_by_id("quto_yes").click()
        driver.find_element_by_id("batch_sale").clear()
        driver.find_element_by_id("batch_sale").send_keys("1.1")
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        driver.find_element_by_id("sale_yes").click()
        driver.find_element_by_id("batch_inventory").clear()
        driver.find_element_by_id("batch_inventory").send_keys("11")
        driver.find_element_by_id("inventory_yes").click()
        driver.find_element_by_xpath("(//input[@type='text'])[10]").click()
        driver.find_element_by_id("batch_skuCode").clear()
        driver.find_element_by_id("batch_skuCode").send_keys("1213441")
        driver.find_element_by_id("code_yes").click()
        driver.find_element_by_id("chkSkuImg").click()
        driver.find_element_by_css_selector("div.col-sm-2 > button.btn.btn-default").click()
        driver.find_element_by_css_selector("a[title=\"e29e34ce01554dccba39836ee9ef6fb8.jpg\"] > img").click()
        driver.find_element_by_id("saveProductImage").click()
        driver.find_element_by_css_selector("div.clearfix > button.btn.btn-default").click()
        driver.find_element_by_css_selector("a[title=\"c60cf67154734fdd87a5571a354140e2.jpg\"] > img").click()
        driver.find_element_by_id("saveProductImage").click()
        driver.find_element_by_id("shareTitle").clear()
        driver.find_element_by_id("shareTitle").send_keys(u"分享设置")
        driver.find_element_by_id("shareContent").clear()
        driver.find_element_by_id("shareContent").send_keys(u"分享内容测试")
        driver.find_element_by_xpath("//button[@onclick=\"openImgSpace('squareShow',5);\"]").click()
        driver.find_element_by_css_selector("a[title=\"c44ba518b7354aef85f9a9c71592ea2f.jpg\"] > img").click()
        driver.find_element_by_css_selector("a[title=\"c44ba518b7354aef85f9a9c71592ea2f.jpg\"] > img").click()
        driver.find_element_by_css_selector("a[title=\"b92ff375862a4ca48d6c912eb7f62566.jpg\"] > img").click()
        driver.find_element_by_css_selector("a[title=\"b4c9559a21ba48959774fcb63ecc8e10.jpg\"] > img").click()
        driver.find_element_by_css_selector("a[title=\"add2a696e4c74325875cfec45f51d7e7.jpg\"] > img").click()
        driver.find_element_by_id("saveProductImage").click()
        driver.find_element_by_xpath("//button[@onclick=\"openImgSpace('rectangleShow',1);\"]").click()
        driver.find_element_by_id("1045_catalogName").click()
        driver.find_element_by_id("1047_catalogName").click()
        driver.find_element_by_css_selector("a[title=\"5c873b7bf3bb95cbbc452c2f935f31ff.jpg\"] > img").click()
        driver.find_element_by_id("saveProductImage").click()
        driver.find_element_by_xpath("(//input[@name='shippingType'])[2]").click()
        driver.find_element_by_xpath("//ul[@id='selectShippingTemplate_listbox']/li").click()
        driver.find_element_by_id("logisticsWeight_2334").clear()
        driver.find_element_by_id("logisticsWeight_2334").send_keys("500")
        driver.find_element_by_xpath("(//input[@type='text'])[36]").click()
        driver.find_element_by_id("logisticsWeight_2504").clear()
        driver.find_element_by_id("logisticsWeight_2504").send_keys("1000")
        driver.find_element_by_xpath("(//input[@type='text'])[38]").click()
        driver.find_element_by_id("logisticsWeight_2523").clear()
        driver.find_element_by_id("logisticsWeight_2523").send_keys("1500")
        driver.find_element_by_name("saleType").click()
        driver.find_element_by_xpath("(//input[@name='stockReduceType'])[2]").click()
        driver.find_element_by_id("toOn").click()
        driver.find_element_by_link_text(u"确定").click()
        driver.find_element_by_xpath("//button[@onclick='addSkuValue();']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
