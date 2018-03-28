#-*- coding: UTF-8 -*-

import os
import hashlib
import preonline.public_login_preonline as plogin
import json
import time


#获取签名两种方式：GET、POST
#GET需要传入url参数+固定key值
#POST需要传入url参数+body参数+固定key值
#通过MakeSign的makeSignForGet、makeSignForPost对外提供

public_key = "94ffa69e31d84f3c1c655e4db605effc"

class MakeSign():

    def __init__(self,body_params):
        self.body_params = body_params

    def makeSignForGet(self):
        url_params = "os=android&osVersion=25&deviceBrand=OD103&appVersion=1.1.0 \
                     &ip=10.0.1.43&lng&lat&deviceId=9ee0aeb206db182a&platform=1&appType=4"
        parents_sign = hashlib.md5(url_params + public_key).hexdigest()
        return parents_sign

    def makeSignForPost(self):
        '''dt = "2018-01-17 14:16:24"
        # 转换成时间数组
        timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp = time.mktime(timeArray)'''
        try:
            url_params = "os=android&osVersion=25&deviceBrand=OD103&appVersion=1.1.0&ip=10.0.1.43&lng&lat&deviceId=9ee0aeb206db182a&platform=1&appType=4&timestamp="
            #url_body1 = "loginNo=%s" % (self.body_params.get("loginNo"))
            #ss = "&"
            #url_body2 = "password=%s" % (self.body_params.get("password"))
            #url_body = ss+url_body1+ss+url_body2+ss

            parents_sign = hashlib.md5(url_params + str(int(round(time.time() * 1000))) + json.dumps(self.body_params) + public_key).hexdigest()
            #parents_sign = hashlib.md5(url_params + str(int(round(timestamp * 1000))) + json.dumps(self.body_params) + public_key).hexdigest()
            #print url_params + str(int(round(time.time() * 1000))) + json.dumps(self.body_params) + public_key
            return parents_sign
            #return parents_sign
        except BaseException,e:
            print "Pls check all params for make sign",e

if __name__=='__main__':
    http_params = {}
    http_query = {"loginNo":"1386666111100",
                    "password":"111100"}

    http_params['loginNo'] = http_query['loginNo']
    http_params['password'] = hashlib.md5(http_query['password']).hexdigest()
    MakeSign(http_params).makeSignForPost()

