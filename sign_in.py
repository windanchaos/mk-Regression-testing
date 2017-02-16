from splinter import Browser
import time, sys
import random
accout = "18781901199"
passport = "miang521"
backgroundURL="http://shop.aiyaohong.com"
productName='回归测试商品'
shortDes='回归测试商品.....'
productCode='11211123'

browser = Browser('chrome')
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

time.sleep(2)
browser.find_by_xpath('//*[@id="addSpecV_0"]').click()
time.sleep(1)
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').click()
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').fill('1L')
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[2]/button').click()
time.sleep(2)
browser.find_by_xpath('//*[@id="addSpecV_0"]/a').click()
time.sleep(1)
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[1]/span/span/input').fill('2L')
browser.find_by_xpath('//*[@id="skuValueWindow"]/div/div/fieldset/div/div[2]/button').click()

# 规格挂牌价格
# 以下4行代码耗费我3天的时间实验验证得出

browser.evaluate_script('document.getElementById("batch_quto").style="display: inline-block; visibility: visible;"')
browser.evaluate_script('document.getElementById("batch_quto").contentEditable = true')
# browser.find_by_xpath('//*[@id="skuShow"]/div[1]/div/div[2]/div[1]/span[2]/span/input[1]').fill(12)
browser.find_by_id('batch_quto').fill("120")
browser.evaluate_script('document.getElementById("batch_quto").style="display: none; visibility: visible;"')


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
