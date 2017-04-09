# -*- coding: UTF-8 -*-
import urllib
import time
from splinter import Browser
import traceback

from selenium.webdriver.common.action_chains import ActionChains

class Crawler:
    def __init__(self):
        #self.url = 'http://image.baidu.com/search/index?ct=201326592&z=&tn=baiduimage&ipn=r&word=%E5%A5%B3%E8%A3%85&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=2&lm=-1&st=-1&fr=&fmq=1491621041308_R&ic=0&se=&sme=&width=640&height=640&face=0'  # url to crawl
        self.url="http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%A5%B3%E8%A3%85&step_word=&hs=0&pn=1&spn=0&di=81519494430&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2761277224%2C163186779&os=3431415753%2C3677206447&simid=3129496258%2C3846151896&adpicid=0&lpn=0&ln=1989&fr=&fmq=1491621041308_R&fm=&ic=0&s=undefined&se=&sme=&tab=0&width=640&height=640&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fd11.yihaodianimg.com%2FN06%2FM00%2F6E%2F09%2FCgQIzlSGcEWAR9UQAAYMqj7WSj452200_640x640.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3F4_z%26e3Byi1_z%26e3Bv54AzdH3Ftpj4AzdH3F98l880nb&gsm=0&rpstart=0&rpnum=0"
        self.img_xpathes = '//*[@id="imgitem"]'  # xpath of img element
        self.download_xpath = '//ul/li/div/div/span/a[@class="down"]'  # xpath of download link element
        self.img_url_dic = {}

        # kernel function

    def launch(self):
        # launch driver
        browser = Browser('chrome')
        browser.driver.maximize_window()
        browser.visit(self.url)
        #browser.driver.implicitly_wait(5)
        #browser.driver.Manage().Timeouts().SetPageLoadTimeout(600);

        for i in range(500):

            #timeload=browser.evaluate_script('window.performance.timing.domLoading-window.performance.timing.connectStart')
            #timeload = browser.evaluate_script('window.performance.timing.domComplete - window.performance.timing.fetchStart')
            #timeload = browser.evaluate_script('window.performance.timing')
            #print(timeload)

            try:
            # if(timeload>1000):
            #     browser.evaluate_script('$(".img-switch-btn").last().click()')
                browser.reload()
                browser.driver.set_page_load_timeout(10)
                browser.driver.set_script_timeout(15)
                if browser.is_element_present_by_text('下载'):
                    browser.find_by_text('下载').first.click()
                else:
                    browser.evaluate_script('$(".img-switch-btn").last().click()')
            except:
                try:
                    browser.evaluate_script('$(".img-switch-btn").last().click()')
                except:
                    traceback.print_exc()
                    pass

            #browser.evaluate_script('$(".img-switch-btn").last().click()')
            time.sleep(1.5)
            if(len(browser.windows)>1):
                browser.windows.current = browser.windows[0]
                browser.windows.current.close_others()
                #如果下载不成功则下一张
                browser.evaluate_script('$(".img-switch-btn").last().click()')
            else:
                browser.evaluate_script('$(".img-switch-btn").last().click()')

        # download_xpath = self.download_xpath
        # img_url_dic = self.img_url_dic
        # imgboxes = browser.evaluate_script('$(".imgbox")')
        #
        # for imgbox in imgboxes:
        #     print(imgbox)
        #     #print(type(imgbox))
        #
        #     ActionChains(browser.driver).click(imgbox).perform()
        #     time.sleep(1)
        #     print(len(browser.windows))
        #     browser.windows.current = browser.windows[1]
        #     browser.find_by_text('下载').first.click()
        #     browser.windows.current = browser.windows[0]
        #     browser.windows.current.close_others()

            # index_of_imgbox = imgboxes.index(imgbox)
            # script ='$(".imgbox")'+'['+str(index_of_imgbox)+']'+'.mouseover()'
            # print(script)
            # browser.evaluate_script(script)
            #ActionChains(browser.driver).click_and_hold(imgbox)
            #ActionChains(browser.driver).move_to_element(imgbox).click_and_hold()

        #    time.sleep(1)
            # browser.evaluate_script('$([title="下载原图"]).click()')



        # for img_xpath in img_xpathes:
        #     browser.find_by_xpath(img_xpath).mouse_over()
        #     browser.find_by_xpath(img_xpath).find_by_id('down').click()

        # 模拟滚动窗口以浏览下载更多图片
        # pos = 0
        # for i in range(10):
        #     pos += i * 500  # 每次下滚500
        #     print('get in for loop')
        #     js = "document.documentElement.scrollTop=%d" % pos
        #     browser.evaluate_script(js)
        #     # get image desc and download
        #     for img_element, link_element in zip(browser.find_by_xpath(img_xpath),
        #                                          browser.find_by_xpath(download_xpath)):
        #         img_desc = img_element.get_attribute('data-desc')  # description of image
        #         img_desc = self.filter_filename_str(img_desc)
        #         print(img_desc)
        #
        #         img_url = link_element.get_attribute('href')  # url of source image
        #         if img_url != None and not img_url_dic.has_key(img_url):
        #             img_url_dic[img_url] = ''
        #             ext = img_url.split('.')[-1]
        #             filename = img_desc + '.' + ext
        #             print(img_desc, img_url)
        #             img_desc, img_url
        #             print('downloading~~~')
        #             urllib.urlretrieve(img_url, './pic/%s' % filename)
        #             time.sleep(1)
        # #browser.windows[0].close()
        #
        # # filter invalid characters in filename

    def filter_filename_str(self, s):
        invalid_set = ('\\', '/', ':', '*', '?', '"', '<', '>', '|', ' ')
        for i in invalid_set:
            s = s.replace(i, '_')
        return s


if __name__ == '__main__':
    crawler = Crawler()
    crawler.launch()