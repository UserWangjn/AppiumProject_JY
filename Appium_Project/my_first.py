#coding=utf-8
#@Author:Administrator
#@date:2019/7/31   11:00


from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.install_app('path/to/my.apk')
# driver.install_app('E:\\JieYue_XQJF_2019-08-02_3.1.2_stg5.apk')

# driver.find_element_by_name("1").click()
driver.find_element_by_id('com.android.calculator2:id/digit_1').click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("del").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()

driver.quit()