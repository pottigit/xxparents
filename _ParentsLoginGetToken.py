#-*- coding: UTF-8 -*-
import os
import requests
import json
import base64
import logging
import time
from logging.handlers import RotatingFileHandler
from MakePublicSign import *
from ReadDBConfig import *
from ConnectMongoDB import *

class ParentsLogin(object):
    def __init__(self,login_url,login_data,login_header):
        self.login_url = login_url
        self.login_data = login_data
        self.login_header = login_header

        self.testRecord = logging.getLogger("ApiTestRecord")
    def init_logging(self):
        self.testRecord = logging.getLogger("ApiTestRecord")
        filelog = RotatingFileHandler("ApiTestRecord.log", maxBytes=20 * 1024 * 1024, backupCount=20)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        filelog.setFormatter(formatter)
        self.testRecord.addHandler(filelog)

        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.testRecord.addHandler(console)

        self.testRecord.setLevel(logging.INFO)

    def LoginRequest(self):

        geter = MakeSign(self.login_data)
        all_sign = geter.makeSignForPost()
        final_url = self.login_url+"&sign="+all_sign
        connection = requests.post(final_url,
                                    data=self.login_data,
                                    headers=self.login_header)
        connection_result = json.loads(connection.text)
        return connection_result,final_url

    # 登录
def getToken(file_path,file_index):
    headers = {
        'Accept-Encoding': 'gzip',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': '192.168.0.215:8084',
        'User-Agent': 'okhttp/3.8.1'
    }

    url1 = "http://192.168.0.215:8084/api/parent/login?"
    url2 = "os=android&osVersion=25&deviceBrand=OD103&appVersion=1.1.0&ip=10.0.1.43&lng&lat&deviceId=9ee0aeb206db182a&platform=1&appType=4"
    url3 = url1 + url2

    handle1 = ReadMongo(file_path,file_index)
    result = handle1.getMongoData()
    server_ip = result[0]
    port = result[1]
    databases = result[2]
    table = result[3]

    conner = ConnectMongoDB(server_ip, port, databases, table)
    conner.runConn()
    more_data = conner.findMoreData()
    for http_query in more_data:
        http_params={
            'password':hashlib.md5(http_query['password']).hexdigest(),
            'loginNo':str(http_query['loginNo'])
        }
        #http_params['password'] = hashlib.md5(http_query['password']).hexdigest()
        #http_params['loginNo'] = http_query['loginNo']

        loginer = ParentsLogin(url3,http_params,headers)
        responseer,final_url= loginer.LoginRequest()
        print responseer
        print responseer['message']
        print final_url
        print http_params

if __name__=='__main__':
    path = './xxparents'
    index = 0
    getToken(path,index)

