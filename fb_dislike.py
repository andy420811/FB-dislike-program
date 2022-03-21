#coding=utf-8
from itertools import count
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By 
from PyQt5 import QtWidgets
from controller import MainWindow_controller
import sys

app = QtWidgets.QApplication(sys.argv)
form = MainWindow_controller()


options = webdriver.ChromeOptions()   #创建浏览
# opt.set_headless()    #无窗口模式

prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)


driver = webdriver.Chrome(options = options)  #创建浏览器对象



driver.get('https://www.facebook.com') #打开网页
#driver.maximize_window()   #最大化窗口
context = driver.find_element(By.ID , 'email')
context.send_keys("{email}}")  #need to change
time.sleep(0.5)     #加载等待

context = driver.find_element(By.ID , 'pass')
context.send_keys("{password}") #need to change

driver.find_element(By.XPATH , "//button[@value='1'][@name='login']").click()
time.sleep(4)

'''context = driver.find_element(By.ID , "approvals_code")
while True:
    AuthCode = input("Enter the code get from phone!\n")
    if input("y/n\n") == 'y':
        break
    
context.send_keys(AuthCode)
time.sleep(0.5)     #加载等待

driver.find_element(By.XPATH , "//button[@value='Continue'][@name='submit[Continue]']").click()
time.sleep(0.5)     #加载等待

driver.find_element(By.XPATH , "//button[@value='Continue'][@name='submit[Continue]']").click()
time.sleep(4)     #加载等待
'''
driver.get('https://www.facebook.com/100003892046177/allactivity?activity_history=false\
            &category_key=LIKEDINTERESTS&manage_mode=false&should_load_landing_page=false')
#form = MainWindow_controller()
#form.show()
start = 0

while True:
    items = driver.find_elements(By.XPATH , "//div[@class = 'l9j0dhe7 btwxx1t3 j83agx80']")
    final = len(items)
    print(items)
    for item in items[start:final]:
        item.location_once_scrolled_into_view
        form.ui.textBrowser.setText(item.text)
        image = item.find_element(By.TAG_NAME , "image")
        form.SetImage(image.get_attribute("xlink:href"))
        form.exec_()
        if form.state == 1:
            BTN1 = item.find_element(By.XPATH , ".//div[@aria-label = 'Action options']" )
            time.sleep(0.1)
            driver.execute_script("(arguments[0]).click()",BTN1)
            time.sleep(0.1)
            BTN2 = item.find_element(By.XPATH , "//div[@role = 'menuitem']" )
            time.sleep(0.1)
            BTN2.click()
            form.state = 0
        else:
            continue
        
        
    start = final
    
