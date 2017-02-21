from splinter import Browser
import time, sys
import random
accout = "18781901199"
passport = "miang521"
backgroundURL="http://shop.aiyaohong.com"
productName='回归测试商品'
shortDes='回归测试商品.....'
productCode='11211123'

# browser = Browser('chrome', fullscreen=True)
browser = Browser('chrome',)
browser.driver.set_window_size(1600, 1000)
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
browser.evaluate_script('$("#chkSkuImg").click()')
# browser.find_by_id("chkSkuImg").click()

browser.evaluate_script('$(".mk-product-body").scrollTop(500)')
browser.evaluate_script('window.scrollTo(0,0)')
# sku 图片设置
browser.find_by_xpath('//*[@id="skuImgTable"]/tbody/tr/td/div[1]/button').click()
time.sleep(0.5)
browser.find_by_text('方图三').click()
time.sleep(0.5)
browser.evaluate_script('$("li[onclick]")[14].click()')
browser.find_by_id("saveProductImage").click()
time.sleep(0.5)
browser.find_by_xpath('//*[@id="skuImgTable"]/tbody/tr/td/div[2]/button').click()
time.sleep(0.5)
browser.find_by_text('方图二').click()
time.sleep(0.5)
browser.evaluate_script('$("li[onclick]")[12].click()')
browser.find_by_id("saveProductImage").click()
time.sleep(0.5)
# 销售库存设置
browser.evaluate_script('$("#displaySoldQty").click()')
browser.evaluate_script('$("#displayInventory").click()')
browser.evaluate_script('$(".mk-product-body").scrollTop(1500)')
# 分享设置
browser.find_by_id("shareTitle").fill(u"自动测试脚本分享设置")
browser.find_by_id("shareContent").fill(u"自动测试脚本发布商品。。。。。。")
browser.find_by_xpath('//*[@id="productInfo"]/div[5]/div[2]/div/div[1]/div/div/button').click()
time.sleep(0.5)
browser.find_by_text('方图二').click()
time.sleep(0.5)
browser.evaluate_script('$("li[onclick]")[11].click()')
time.sleep(0.5)
browser.find_by_id("saveProductImage").click()
time.sleep(0.5)

# 商品图片设置
#  宽图
browser.evaluate_script('$(".mk-product-body").scrollTop(1800)')
browser.find_by_xpath('//*[@id="productInfo"]/div[6]/div[2]/div/div[1]/div/button').click()
time.sleep(0.5)
browser.find_by_text('方图三').click()
time.sleep(0.5)
browser.evaluate_script('$("li[onclick]")[1].click()')
browser.evaluate_script('$("li[onclick]")[13].click()')
browser.evaluate_script('$("li[onclick]")[7].click()')
browser.evaluate_script('$("li[onclick]")[2].click()')
browser.find_by_xpath('//*[@id="saveProductImage"]').click()
time.sleep(0.5)
# 长图
browser.find_by_xpath('//*[@id="productInfo"]/div[6]/div[2]/div/div[3]/div/button').click()
time.sleep(0.5)
browser.find_by_text('长图一服装').click()
time.sleep(0.5)
browser.evaluate_script('$("li[onclick]")[14].click()')
browser.find_by_xpath('//*[@id="saveProductImage"]').click()
time.sleep(0.5)
browser.evaluate_script('$(".mk-product-body").scrollTop(2000)')
# 运费设置
browser.find_by_xpath("(//input[@name='shippingType'])[2]").click()
browser.find_by_text('请选择').click()
time.sleep(0.5)
browser.find_by_text('四川免运').click()

# 物流重量，使用jquery填充和单击输入框
browser.evaluate_script('$("input[id^=\'logisticsWeight\']").first().val("500")')
browser.evaluate_script('$("input[class=\'k-formatted-value noEdit k-input\']").first().click()')
browser.evaluate_script('$("input[id^=\'logisticsWeight\'").last().val("1500")')
browser.evaluate_script('$("input[class=\'k-formatted-value noEdit k-input\']").last().click()')

browser.find_by_name("saleType").click()
browser.find_by_xpath("(//input[@name='stockReduceType'])[2]").click()
browser.find_by_id("toOn").click()
time.sleep(0.5)
browser.find_by_xpath('/html/body/div[1]/div/div[3]/a').click()



