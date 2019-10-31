#coding=utf-8
#@Author:Administrator
#@date:2019/8/12   16:05

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  #翻译：预期的条件
import time
from Appium_Project.common import swipeLeft

sever = 'http://localhost:4723/wd/hub'
# 翻译：所需的能力
desired_caps= {
    'platformName':'Android',
    'platformVersion':'4.4',
    'deviceName':'xiaomi-mix_2',
    'appPackage':'com.jieyue.jieyue.test',
    'appActivity':'com.jieyue.jieyue.ui.activity.SplashActivity'
}
# desired_caps= {
#     'platformName':'Android',
#     'platformVersion':'7.1',
#     'deviceName':'127.0.0.1:62001',
#     'appPackage':'com.jieyue.jieyue.test',
#     'appActivity':'com.jieyue.jieyue.ui.activity.SplashActivity'
# }

# 驱动
driver = webdriver.Remote(sever,desired_caps)
wait = WebDriverWait(driver,20)

time.sleep(1)
# 向左滑动欢迎页面，进入主页面
swipeLeft(driver,2)
# 点击开启美好生活  presence_of_element_located翻译:存在  元素   定位
start_btn = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/tv_enter_into')))
start_btn.click()
time.sleep(1)
# 获取允许通讯录权限按钮
try:
    allow_btn = wait.until(EC.presence_of_element_located((By.ID,'android:id/button1')))
    allow_btn.click()
    allow_btn.click()
    time.sleep(2)
except:
    pass

# 获取我的按钮
my_btn = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/mine_icon')))
my_btn.click()
# 获取手机号文本框
user_text = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/login_pho_edittext')))
user_text.send_keys('15811112222')
# 获取登录下一步按钮
login_pho_btn = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/login_button')))
login_pho_btn.click()
# 获取密码文本框
# pwd_text = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/login_pwd_edittext')))
# pwd_text.send_keys('q1111111')
# 获取登录按钮
# login_btn = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/login_button')))
# login_btn.click()

# 获取短信验证码登录按钮
mes_login_btn = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/tv_login_type')))
mes_login_btn.click()
time.sleep(1)
# 获取获取验证码按钮
get_mes_btn = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/login_getcode')))
get_mes_btn.click()
# 获取输入短信验证码输入框
inp_mes_text = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/login_smcode_edittext')))
inp_mes_text.send_keys('111111')
# 获取登录按钮
login_btn = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/login_button')))
login_btn.click()
#获取跳过按钮
jump_btn = wait.until(EC.presence_of_element_located((By.ID,'com.jieyue.jieyue.test:id/right_text')))
jump_btn.click()



time.sleep(5)


# driver.quit()