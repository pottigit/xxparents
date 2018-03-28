#-*- coding: UTF-8 -*-

from ConnectMongoDB import *
from HttpBasePublic import *
from ParentsLogin import *

#创建获取token方法，内部创建登录类对象后调用家长端公共登录方法获取返回token值
def touchSendCodeBind(login_no, telephone, token):

    #http request element(body, url)
    http_params = {
                  "userNo": login_no,
                  "phone": telephone}
    api_url = "http://192.168.0.215:8084/api/sms/cellphone/bind?"
    params_url = "os=android&osVersion=25&deviceBrand=OD103&appVersion=1.1.0&ip=10.0.1.43&lng&lat&deviceId=9ee0aeb206db182a&platform=1&appType=4&timestamp="
    times = str(int(round(time.time() * 1000)))
    request_url = api_url+params_url+times
    httper = HttpBase('GET', request_url, http_params, token)
    # 使用GET方法请求校区列表接口
    status_code, res = httper.httpRequest()

    if res['status'] == 200:
        print "touch verify code successfully"
    else:
        print "not touch verify code"
