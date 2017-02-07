from splinter import Browser

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

browser.find_by_text('商品管理').click()
browser.find_by_text('商品仓库').click()
browser.find_by_text('发布商品').click()
browser.find_by_id('item_2').click()
browser.find_by_text('下一步').click()

browser.find_by_id('productName').fill(productName)
browser.find_by_id('shortDes').fill(shortDes)
browser.find_by_id('productCode').fill(productCode)

browser.find_by_text('添加规格项目').click()
browser.find_by_text('添加规格').click()
# browser.find_by_name('k-widget k-window').find_by_name('k-input').fill('尺寸')
# browser.find_by_value('确定').click()
# browser.find_by_name('link-primary noEdit').click()
# browser.fill('k-input', '尺寸')
# browser.find_by_value('添加').click()
# browser.find_by_name('k-icon k-i-arrow-s').click()
# browser.find_by_text('L').click()
