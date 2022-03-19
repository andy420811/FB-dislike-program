#coding=utf-8
import imp
from os import system
import sys
from requests_toolbelt import ImproperBodyPartContentException
from selenium import webdriver
import time
import re
import selenium
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PyQt5 import QtWidgets
from controller import MainWindow_controller
import sys
# Python Program to find element by text

#import webdriver
from selenium import webdriver

#import time
from time import sleep

# create webdriver object
driver = webdriver.Chrome()

# get the website
driver.get("http://bit.ly/vinayakgfg")

# sleep for some time
sleep(3)

# get element through text
driver.find_element_by_xpath("// a[contains(text(),\
'5 CHEAP HOLIDAY')]").click()

# sleep for some time
sleep(4)
