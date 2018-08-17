# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:55:36 2018

@author: Toby

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser=webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()
browser.get("http://www.google.com")
click=browser.find_element_by_id("gb_70").click()
email=browser.find_element_by_css_selector(".whsOnd.zHQkBf").send_keys("paul33931029@gmail.com"+Keys.ENTER)
sleep(3)
password=browser.find_element_by_css_selector(".whsOnd.zHQkBf").send_keys("paul33931029"+Keys.ENTER)
