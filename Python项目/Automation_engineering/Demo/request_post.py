# -*- coding:utf-8 -*-
import requests
import json
url = 'http://81.71.41.57:8800/manager/api/user/login_action'
payload = {
'username':'admin',
'password': '123456',
'exam_area_id': '2558',
'sms_code':'',
'device_id':'',
'verifyCode':'',
'phone':'',
'login_type': '1'
            }
response = requests.request('post',url,data=payload)
print(response.text)
