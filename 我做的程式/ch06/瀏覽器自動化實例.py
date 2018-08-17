# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:28:17 2018

@author: Toby
"""

from selenium import webdriver
browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://opendata.epa.gov.tw/Data/Contents/AQI/")
browser.find_element_by_class_name("color_a").click()
browser.find_element_by_class_name("color_b").click()
browser.find_element_by_class_name("color_c").click()