#coding=utf-8
#@Author:Administrator
#@date:2019/8/6   17:23

from appium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#app启动参数  # 翻译：所需的能力Desired Capabilities
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'xiaomi-mix_2'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = '.Calculator'

#驱动
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver,20)

# 获取允许通讯录权限按钮
allow_btn = wait.until(EC.presence_of_element_located((By.ID,'android:id/button1')))
# 点击允许按钮
allow_btn.click()
allow_btn.click()
# 获取登录按钮
login_btn = wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/edu')))
# 点击登录按钮
login_btn.click()
# 获取用微信号登录按钮
use_wx_btn = wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/cvf')))
use_wx_btn.click()
# 获取账号文本框
# user_text = wait.until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText')))
user_text = wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/li')))
user_text.send_keys('test123')
# com.tencent.mm:id/li
# com.tencent.mm:id/li
time.sleep(6)


# driver.find_element_by_id('android:id/button1').click()
# time.sleep(2)
# driver.find_element_by_id('android:id/button1').click()
# time.sleep(2)
# driver.find_element_by_id('com.tencent.mm:id/edu').click()
# time.sleep(2)

# el4 = driver.find_element_by_id("com.tencent.mm:id/cvf")
# el4.click()
# el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText")
# el5.send_keys("test123")
# el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
# el6.send_keys("123456")
# el7 = driver.find_element_by_id("com.tencent.mm:id/cvg")
# el7.click()

time.sleep(6)


driver.quit()
