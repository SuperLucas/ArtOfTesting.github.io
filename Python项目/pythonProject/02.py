# coding=utf-8

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'platformVersion': '7.1.2',
                # apk包名
                'appPackage': 'com.jinqikeji.tell',
                # apk的launcherActivity
                'appActivity': 'com.jinqikeji.tell.MainActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_xpath("//*[@text=同意]")
driver.find_element_by_xpath("//*[@text='通讯录']")

# # 元素定位，注意我这里的写法，用的是find_elements_by_class_name，另外还要加索引
# agree_continue_class = "android.widget.Button"
# WebDriverWait(driver, 10, 1).until(EC.visibility_of_all_elements_located((MobileBy.CLASS_NAME, agree_continue_class)))
# driver.find_elements_by_class_name(agree_continue_class)[1].click()
