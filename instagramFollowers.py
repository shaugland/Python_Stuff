#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox()

driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

time.sleep(2)

email = driver.find_elements_by_tag_name("input")

time.sleep(1)

# First one is for username, second for password
email[0].send_keys("")
email[1].send_keys("")

log_in = driver.find_elements_by_tag_name("button")
time.sleep(1)
try:
    while(log_in[1]):
        log_in[1].click()
        time.sleep(1)
except:
    time.sleep(5)

# Sometimes instagram gives me a popup, this is to get rid of it
buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
buttons[0].click()

time.sleep(1)

# Going to go to the find people page so we can follow people 
driver.find_element_by_xpath("//span[@aria-label='Find People']").click()

see_all = driver.find_elements_by_xpath("//*[contains(text(), 'See All')]")
see_all[0].click()

time.sleep(1)

# Function so that we can click a button after every 30 seconds
# Can probably go faster but for whatever reason instagram doesn't like how often I click buttons
# Maybe it's because it thinks this is a bot or something....
def following():
    follow_buttons = driver.find_elements_by_xpath("//button[text()='Follow']")

    for i in range(len(follow_buttons)):
        follow_buttons[i].click()
        time.sleep(30)


# Bot is sleepy after all that work
time.sleep(5)
# Time to go to work again
while(True):
    following()
    # This is to load another page since the page won't load more 
    # buttons unless we scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Bot is still sleepy
    time.sleep(10)
