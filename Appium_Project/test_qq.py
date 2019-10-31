#coding=utf-8
#@Author:Administrator
#@date:2019/10/29   16:59

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

sever = 'http://localhost:4723/wd/hub'
# 翻译：所需的能力
desired_caps= {
    'platformName':'Android',
    'platformVersion':'4.4',
    'deviceName':'xiaomi-mix_2',
    'appPackage':'com.tencent.mobileqq',
    'appActivity':'com.tencent.mobileqq.activity.SplashActivity'
}

driver = webdriver.Remote(sever,desired_caps)
wait = WebDriverWait(driver,20)

try:
    # 点击同意服务协议和隐私政策
    agree_btn = wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mobileqq:id/dialogRightBtn')))
    agree_btn.click()
except:
    pass
# 点击登录按钮
login_btn = wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mobileqq:id/btn_login')))
login_btn.click()

# 输入用户名
user_name = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@text="QQ号/手机号/邮箱"]')))
print('user_name',user_name)
user_name.click()
user_name.send_keys('963454585')
# 输入密码
pwd = wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mobileqq:id/password')))
pwd.send_keys('wangjianing951')

# 点击登录按钮
login = wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mobileqq:id/login')))
login.click()


