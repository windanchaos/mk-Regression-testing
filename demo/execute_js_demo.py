from splinter import Browser
import time
import sys

# copy t.html to tomcat/webapp/ROOT/
browser = Browser('chrome')
browser.visit("http://localhost:8080/t.html")
time.sleep(2)
browser.evaluate_script('document.getElementById("p1").style.fontFamily="Arial"')
time.sleep(2)
browser.evaluate_script('document.getElementById("p2").style.color="red"')
time.sleep(2)
browser.evaluate_script('document.getElementById("p3").style.fontFamily="Arial"')
browser.evaluate_script('document.getElementById("p3").style.color="gray"')
time.sleep(2)
browser.evaluate_script('document.getElementById("p4").style.fontSize="30px"')
time.sleep(2)
browser.evaluate_script('document.getElementById("p1").class="bodyChange"')
time.sleep(2)
browser.evaluate_script('document.getElementById("p2").class="body"')
