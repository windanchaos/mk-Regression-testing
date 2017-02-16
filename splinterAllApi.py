# Example
from splinter import Browser
with Browser() as browser:
    # Visit URL
    url = "http://www.google.com"
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_name('btnG')
    # Interact with elements
    button.click()
    if browser.is_text_present('splinter.readthedocs.io'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")
# browser type
browser = Browser('chrome')
browser = Browser('firefox')
browser = Browser('zope.testbrowser')
# Managing Windows
browser.windows              # all open windows
browser.windows[0]           # the first window
browser.windows["window_name"] # the window_name window
browser.windows.current      # the current window
browser.windows.current = browser.windows[3]  # set current window to window 3

window = browser.windows[0]
window.is_current            # boolean - whether window is current active window
window.is_current = True     # set this window to be current window
window.next                  # the next window
window.prev                  # the previous window
window.close()               # close this window
window.close_others()        # close all windows except this one
# Reload/back/forward a page
browser.reload()
browser.back()
browser.forward()

# get page tile /page content /url
browser.title
browser.html
browser.url

# change Browser User-Agent
b = Browser(user_agent="Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)")

# Finding elements，returns a list with the found elements
browser.find_by_css('h1')
browser.find_by_xpath('//h1')
browser.find_by_tag('h1')
browser.find_by_name('name')
browser.find_by_text('Hello World!')
browser.find_by_id('firstheader')
browser.find_by_value('query')
# get element
first_found = browser.find_by_name('name').first
last_found = browser.find_by_name('name').last
second_found = browser.find_by_name('name')[1]

# Get value of an element
browser.find_by_css('h1').first.value

# Clicking links,return the first link
browser.click_link_by_href('http://www.the_site.com/my_link')
browser.click_link_by_partial_href('my_link')
browser.click_link_by_text('my link')
browser.click_link_by_partial_text('part of link text')
browser.click_link_by_id('link_id')

# element is visible or invisible
browser.find_by_css('h1').first.visible

#fill content
browser.find_by_id('productName').fill('splinter - python acceptance testing for web applications')
browser.fill('q', 'splinter - python acceptance testing for web applications')

# Verifying if element has a className
browser.find_by_css('.content').first.has_class('content')
# click button
browser.find_by_name('send').first.click()
browser.find_link_by_text('my link').first.click()

# Mouse
browser.find_by_tag('h1').mouse_over()
browser.find_by_tag('h1').mouse_out()
browser.find_by_tag('h1').click()
browser.find_by_tag('h1').double_click()
browser.find_by_tag('h1').right_click()
# Mouse drag and drop
draggable = browser.find_by_tag('h1')
target = browser.find_by_css('.container')
draggable.drag_and_drop(target)

# Interacting with forms
browser.fill('query', 'my name')
browser.attach_file('file', '/path/to/file/somefile.jpg')
browser.choose('some-radio', 'radio-value')
browser.check('some-check')
browser.uncheck('some-check')
browser.select('uf', 'rj')

# screenshot
browser.driver.save_screenshot('your_screenshot.png')
# 看不太懂
# trigger JavaScript events, like KeyDown or KeyUp, you can use the type method.
browser.type('type', 'typing text')
'''
 If you pass the argument slowly=True to the type method you can interact with the page on every key pressed. Useful for
'''
# testing field's auto completion (the browser will wait until next iteration to type the subsequent key).
for key in browser.type('type', 'typing slowly', slowly=True):
    pass # make some assertion here with the key object :)

# You can also use type and fill methods in an element:

browser.find_by_name('name').type('Steve Jobs', slowly=True)
browser.find_by_css('.city').fill('San Francisco')

# Dealing with HTTP status code and exceptions
browser.visit('http://cobrateam.info')
browser.status_code.is_success()  # True
browser.status_code == 200  # True
browser.status_code.code  # 200
# try:
# browser.visit('http://cobrateam.info/i-want-cookies')
# except HttpResponseError, e:
# print "Oops, I failed with the status code %s and reason %s" % (e.status_code, e.reason)

# test
# Cookies manipulation
browser.cookies.add({'whatever': 'and ever'}) # add a cookie
browser.cookies.all() # retrieve all cookies
browser.cookies.delete('mwahahahaha')  # deletes the cookie 'mwahahahaha'
browser.cookies.delete('whatever', 'wherever')  # deletes two cookies
browser.cookies.delete()  # deletes all cookies

# Frames, alerts and prompts
# Using iframes，You can use the get_iframe method and the with statement to interact with iframes. You can pass the
# iframe's name, id, or index to get_ifram

with browser.get_iframe('iframemodal') as iframe:
    iframe.do_stuff()

# Chrome support for alerts and prompts is new in Splinter 0.4.Only webdrivers (Firefox and Chrome) has support for
# alerts and prompts.
alert = browser.get_alert()
alert.text
alert.accept()
alert.dismiss()

prompt = browser.get_alert()
prompt.text
prompt.fill_with('text')
prompt.accept()
prompt.dismiss()
# use the with statement to interacte with both alerts and prompts
with browser.get_alert() as alert:
    alert.do_stuff()


# Executing javascript
browser.execute_script("$('body').empty()")
browser.evaluate_script("4+4") == 8

# Matchers
browser = Browser()
browser.visit('https://splinter.readthedocs.io/')
browser.is_text_present('splinter')  # True
browser.is_text_present('splinter', wait_time=10)   # True, using wait_time
browser.is_not_present('text not present')  # True

browser.is_element_present_by_css('h1')
browser.is_element_present_by_xpath('//h1')
browser.is_element_present_by_tag('h1')
browser.is_element_present_by_name('name')
browser.is_element_present_by_text('Hello World!')
browser.is_element_not_present_by_id('firstheader')
browser.is_element_not_present_by_value('query')
browser.is_element_present_by_value('query', wait_time=10)