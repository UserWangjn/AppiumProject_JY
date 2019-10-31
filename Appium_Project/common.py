#coding=utf-8
#@Author:Administrator
#@date:2019/8/14   18:13

import time

# 向左滑动方法
def swipeLeft(driver,n):
    '''
    :param driver:
    :param n: 滑动次数
    :return:
    '''
    # 获取屏幕的size
    size = driver.get_window_size()
    # print('size:', size)
    # 获取屏幕的宽度
    width = size['width']
    # print('width:', width)
    # 获取屏幕高度
    height = size['height']
    # print('height:', height)

    # 执行滑屏操作，向左滑动
    x1 = width * 0.8
    x2 = width * 0.25
    y1 = height * 0.5
    time.sleep(3)
    for i in range(n):
        driver.swipe(x1, y1, x2, y1)
        time.sleep(3)