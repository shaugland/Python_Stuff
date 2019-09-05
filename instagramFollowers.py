#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox()

driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

time.sleep(2)

email = driver.find_elements_by_tag_name("input")

time.sleep(1)
email[0].send_keys("andyfromtheoffice2")
email[1].send_keys("merkur34c")

log_in = driver.find_elements_by_tag_name("button")
time.sleep(1)
try:
    while(log_in[1]):
        log_in[1].click()
        time.sleep(1)
except:
    time.sleep(5)

buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")

buttons[0].click()

time.sleep(1)

driver.find_element_by_xpath("//span[@aria-label='Find People']").click()

see_all = driver.find_elements_by_xpath("//*[contains(text(), 'See All')]")
see_all[0].click()

time.sleep(1)

def following():
    follow_buttons = driver.find_elements_by_xpath("//button[text()='Follow']")

    for i in range(len(follow_buttons)):
        follow_buttons[i].click()
        time.sleep(30)


time.sleep(5)
while(True):
    following()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
