#-*- coding: UTF-8 -*-
import requests
import json
import simplejson
import time
import logging
from logging.handlers import RotatingFileHandler
from MakePublicSign import *
from ReadDBConfig import *
from ConnectMongoDB import *
from decodeSecret import *

token_json = {"ptoken":''}

#创建登录类
class ParentsLogin(object):
    #默认初始化方法
    def __init__(self,login_url,login_data,login_header):
        self.login_url = login_url
        self.login_data = login_data
        self.login_header = login_header

        self.testRecord = logging.getLogger("qa_parents_record")
    #初始化日志记录方法
    def init_logging(self):
        self.testRecord = logging.getLogger("qa_parents_record")
        filelog = RotatingFileHandler("qa_parents_record.log", maxBytes=20 * 1024 * 1024, backupCount=20)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        filelog.setFormatter(formatter)
        self.testRecord.addHandler(filelog)

        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.testRecord.addHandler(console)

        self.testRecord.setLevel(logging.INFO)
    #创建家长端公共登录方法
    def LoginRequest(self):
        #调用生成签名类，创建geter对象后再调用签名生成方法获取sign
        geter = MakeSign(self.login_data)
        all_sign = geter.makeSignForPost()
        final_url = self.login_url+"&sign="+all_sign
        #调用requests库Post方法创建登录
        connection = requests.post(final_url,
                                    data=json.dumps(self.login_data),
                                    headers=self.login_header)
        connection_result = json.loads(connection.text)
        return connection_result

#创建插入token到mongoDB方法
def setToken(file_path,file_index,token_data):
    try:
        dbserver, dbport, dbdatabase, dbtable = ReadMongo(file_path, file_index).getMongoData()
        conn = ConnectMongoDB(dbserver, dbport, dbdatabase, dbtable)
        conn.runConn()
        token_json['ptoken'] = token_data
        conn.insertData(token_json)
        #ParentsLogin().testRecord.info("clear old token successfully")

    except conn,e:
        print "DB error",e

#创建清空mongoDB中token方法
def clearToken(file_path,file_index):
    try:
        dbserver, dbport, dbdatabase, dbtable = ReadMongo(file_path, file_index).getMongoData()
        conn = ConnectMongoDB(dbserver, dbport, dbdatabase, dbtable)
        conn.runConn()
        conn.deleteData()
    except conn,e:
        print "DB error",e

#创建获取token方法，内部创建登录类对象后调用家长端公共登录方法获取返回token值
def getToken(file_path,file_index):
    headers = {
        'Accept-Encoding':'gzip',
        'Connection':'keep-alive',
        'Content-Type':'application/json;charset=UTF-8',
        'Host':'192.168.0.215:8084',
        'User-Agent':'okhttp/3.8.1'}
    http_params = {
                  "password":hashlib.md5('888800').hexdigest(),
                  "loginNo":"1353333888800"}
    api_url = "http://192.168.0.215:8084/api/parent/login?"
    params_url = "os=android&osVersion=25&deviceBrand=OD103&appVersion=1.1.0&ip=10.0.1.43&lng&lat&deviceId=9ee0aeb206db182a&platform=1&appType=4&timestamp="
    times = str(int(round(time.time() * 1000)))
    request_url = api_url+params_url+times
    #创建登录类对象
    loginer = ParentsLogin(request_url,http_params,headers)
    #对象调用LoginRequest方法获取http返回response
    responser = loginer.LoginRequest()
    loginer.init_logging()
    if responser['status'] == 200:
        token = responser['data']['token']
        if token:
            setToken(file_path, file_index, token)
            loginer.testRecord.info("get token successfully")
        else:
            loginer.testRecord.info("get token is null")
        #time.sleep(15)
        #clearToken(file_path,file_index)
    else:
        print responser['message']
if __name__=='__main__':
    path = './xxparents'
    index = 0
    clearToken(path,index)
    getToken(path,index)