from splinter import Browser
import time, sys
import random
accout = "10052"
passport = "miang521"
backgroundURL="https://shop.maike51.com"
productName='回归测试商品'
shortDes='回归测试商品.....'
productCode='11211123'

# browser = Browser('chrome', fullscreen=True)
browser = Browser('chrome',)
browser.visit(backgroundURL)
browser.fill('account', accout)
browser.fill('password', passport)
browser.find_by_value('登    录').click()
print(browser.cookies.all())
print(browser.windows.current)
browser.find_by_text('商品管理').click()
browser.find_by_text('商品仓库').click()
browser.find_by_text('发布商品').click()
browser.find_by_id('item_2').click()
browser.find_by_text('下一步').click()

browser.find_by_id('productName').fill(productName)
browser.find_by_id('shortDes').fill(shortDes)
browser.find_by_id('productCode').fill(productCode)

# 商品规格
browser.find_by_text('添加规格项目').click()
browser.find_by_text('添加规格').click()
browser.find_by_xpath('//*[@id="addSkuWindow"]/div/div/fieldset[1]/div/div/span/span/input').fill('净含量')
browser.find_by_xpath('//*[@id="toAddSku"]').click()

time.sleep(1)
browser.find_by_xpath('//*[@id="addSpecV_0"]').click()
time.sleep(1)
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').click()
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').fill('1L')
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[2]/button').click()
time.sleep(1)
browser.find_by_xpath('//*[@id="addSpecV_0"]/a').click()
time.sleep(1)
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').fill('2L')
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[2]/button').click()

# 规格挂牌价格
# 以下4行代码耗费我3天的时间实验验证得出

browser.evaluate_script('document.getElementById("batch_quto").style="display: inline-block; visibility: visible;"')
browser.find_by_id('batch_quto').fill("120")
browser.evaluate_script('document.getElementById("batch_quto").style="display: none; visibility: visible;"')
time.sleep(1)
browser.find_by_xpath('//*[@id="quto_yes"]').click()

browser.evaluate_script('document.getElementById("batch_sale").style="display: inline-block; visibility: visible;"')
browser.find_by_id('batch_sale').fill("1.12")
browser.evaluate_script('document.getElementById("batch_sale").style="display: none; visibility: visible;"')
browser.find_by_id("sale_yes").click()

browser.evaluate_script('document.getElementById("batch_inventory").style="display: inline-block; visibility: visible;"')
browser.find_by_id('batch_inventory').fill("1233")
browser.evaluate_script('document.getElementById("batch_inventory").style="display: none; visibility: visible;"')
browser.find_by_id("inventory_yes").click()

browser.find_by_id("batch_skuCode").fill("1213441")
browser.find_by_id("code_yes").click()
time.sleep(1)
browser.evaluate_script('document.getElementById("skuImgTable").className="table table-bordered"')
# browser.find_by_id("chkSkuImg").click()

browser.evaluate_script('window.scrollBy(0,1000)')
browser.evaluate_script('window.scrollTo(0,1000)')
browser.find_by_xpath('//*[@id="skuImgTable"]/tbody/tr/td/div[1]/button').click()



browser.find_by_css_selector("a[title=\"e29e34ce01554dccba39836ee9ef6fb8.jpg\"] > img").click()
browser.find_by_id("saveProductImage").click()

browser.find_by_by_xpath('//*[@id="skuImgTable"]/tbody/tr/td/div[2]/button').click()
time.sleep(1)
browser.find_by_css_selector("a[title=\"c60cf67154734fdd87a5571a354140e2.jpg\"] > img").click()
browser.find_by_id("saveProductImage").click()
browser.find_by_id("shareTitle").fill(u"分享设置")

browser.find_by_id("shareContent").fill(u"分享内容测试")
browser.find_by_xpath("//button[@onclick=\"openImgSpace('squareShow',5);\"]").click()
browser.find_by_css_selector("a[title=\"c44ba518b7354aef85f9a9c71592ea2f.jpg\"] > img").click()
browser.find_by_css_selector("a[title=\"c44ba518b7354aef85f9a9c71592ea2f.jpg\"] > img").click()
browser.find_by_css_selector("a[title=\"b92ff375862a4ca48d6c912eb7f62566.jpg\"] > img").click()
browser.find_by_css_selector("a[title=\"b4c9559a21ba48959774fcb63ecc8e10.jpg\"] > img").click()
browser.find_by_css_selector("a[title=\"add2a696e4c74325875cfec45f51d7e7.jpg\"] > img").click()
browser.find_by_id("saveProductImage").click()
browser.find_by_xpath("//button[@onclick=\"openImgSpace('rectangleShow',1);\"]").click()
browser.find_by_id("1045_catalogName").click()
browser.find_by_id("1047_catalogName").click()
browser.find_by_css_selector("a[title=\"5c873b7bf3bb95cbbc452c2f935f31ff.jpg\"] > img").click()
browser.find_by_id("saveProductImage").click()
browser.find_by_xpath("(//input[@name='shippingType'])[2]").click()
browser.find_by_xpath("//ul[@id='selectShippingTemplate_listbox']/li").click()
browser.find_by_id("logisticsWeight_2334").fill("500")
browser.find_by_xpath("(//input[@type='text'])[36]").click()
browser.find_by_id("logisticsWeight_2504").fill("1000")
browser.find_by_xpath("(//input[@type='text'])[38]").click()
browser.find_by_id("logisticsWeight_2523").fill("1500")
browser.find_by_name("saleType").click()
browser.find_by_xpath("(//input[@name='stockReduceType'])[2]").click()
browser.find_by_id("toOn").click()
browser.find_by_link_text(u"确定").click()
browser.find_by_xpath("//button[@onclick='addSkuValue();']").click()


#browser.find_by_xpath("(//input[@type='text'])[6]").click()
# browser.find_by_xpath('//*[@id="skuShow"]/div[1]/div/div[2]/div[1]/span[2]/span/input[1]').fill(12)
# browser.find_by_xpath('//*[@id="quto_yes"]').click()
# # 规格售卖价格
# browser.find_by_xpath('//*[@id="skuShow"]/div[1]/div/div[2]/div[2]/span[2]/span/input[1]').fill('1.2')
# browser.find_by_xpath('//*[@id="sale_yes"]').click()
# # 库存
# browser.find_by_xpath('//*[@id="skuShow"]/div[1]/div/div[2]/div[3]/span[2]/span/input[1]').fill('1.2')
# browser.find_by_xpath('//*[@id="inventory_yes"]').click()
# # sku编码
# browser.find_by_xpath('//*[@id="batch_skuCode"]').fill('21212')
# browser.find_by_xpath('//*[@id="code_yes"]').click()
#
# # 销售记录/购买记录，库存显示设置
# time.sleep(1)
#
# browser.find_by_xpath('//*[@id="productInfo"]/div[4]/div[2]/div[2]/div[4]/label[1]').click()
# browser.find_by_xpath('//*[@id="productInfo"]/div[4]/div[2]/div[2]/div[4]/label[1]').click()
#
# # 分享设置
# browser.find_by_xpath('//*[@id="productInfo"]/div[5]/div[2]/div/div[1]/div/div/button').click()
# time.sleep(2)
# browser.find_by_xpath('//*[@id="1048_catalogName"]').click()
# # 随机选取图片
# imgNo = random.random(1, 15)
# imgXpath = "\'//*[@id=\"listView\"]/li[" + imgNo + "]/div[1]/a/img"
# print(imgXpath)
# browser.find_by_xpath(imgXpath).click()
# browser.find_by_xpath('//*[@id="saveProductImage"]').click()
#
#
#
