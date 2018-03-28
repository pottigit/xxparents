#-*- coding: UTF-8 -*-
import os
import sys
import json
import nose
import time
import time
import logging
from logging.handlers import RotatingFileHandler
from ConnectMongoDB import *
from HttpBasePublic import *

class TestCreateOrder():

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

    def setup(self):
        self.init_logging()
        self.dbserver = "127.0.0.1"
        self.dbport = 27017
        self.dbdatabase = "xstudyparents"
        self.dbtable = "createOrder"
        self.dbtable2 = "orderNoInfo"
        self.payload = {}
        self.token_dbtable = "public_token"

        api_url = "http://192.168.0.215:8084/api/parent/createOrder?"
        params_url = "os=android&osVersion=25&deviceBrand=OD103&appVersion=1.2.0&ip=10.0.1.43&lng&lat&deviceId=9ee0aeb206db182a&platform=1&appType=4&userno=1351111888800&timestamp="
        times = str(int(round(time.time() * 1000)))
        self.url = api_url + params_url + times
        #定义订单号信息，获取订单号信息后存储DB
        self.orderNoInfo = {}

        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.token_dbtable)
            self.conn.runConn()
            dic_token = self.conn.findOneData()
            self.token = dic_token['ptoken']

        except self.conn, e:
            print "DB error", e

    def tearDown(self):
        #self.testRecord.info("Logo config test is over")
        pass

    def testCreateOrderNoPaysource(self):
        """
        [createOrder] create order without pay source
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 1})
            self.payload = {'userId': ListData["userId"], 'paySource': ListData["paySource"], 'list': ListData["list"]}
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            #self.testRecord.info(httper.url)
            #self.testRecord.info(httper.token)
            #self.testRecord.info(self.payload)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False
        except self.conn,e:
            print "DB error",e

    def testCreateOrderInvalidPaysource(self):
        """
        [createOrder] create order with invalid paySource
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 2})
            self.payload = {'userId': ListData["userId"], 'paySource': ListData["paySource"], 'list': ListData["list"]}
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            #self.testRecord.info(httper.url)
            #self.testRecord.info(httper.token)
            #self.testRecord.info(self.payload)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False
        except self.conn,e:
            print "DB error",e

    def testCreateOrderByAppNoCourseid(self):
        """
        [createOrder] create order by app and without courseid list
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 3})
            self.payload = {'userId': ListData["userId"], 'paySource': ListData["paySource"], 'list': ListData["list"]}
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            #self.testRecord.info(httper.url)
            #self.testRecord.info(httper.token)
            #self.testRecord.info(self.payload)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False
        except self.conn,e:
            print "DB error",e

    def testCreateOrderByServerNoCourseid(self):
        """
        [createOrder] create order by server and without courseid list
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 4})
            self.payload = {'userId': ListData["userId"], 'paySource': ListData["paySource"], 'list': ListData["list"]}
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            #self.testRecord.info(httper.url)
            #self.testRecord.info(httper.token)
            #self.testRecord.info(self.payload)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False
        except self.conn,e:
            print "DB error",e


    def testCreateOrderByH5Nocourseid(self):
        """
        [createOrder] create order by H5 and without courseid list
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 5})
            self.payload = {'userId': ListData["userId"], 'paySource': ListData["paySource"], 'list': ListData["list"]}
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            #self.testRecord.info(httper.url)
            #self.testRecord.info(httper.token)
            #self.testRecord.info(self.payload)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False
        except self.conn,e:
            print "DB error",e

    def testCreateOrderByApp(self):
        """
        [createOrder] create order by App
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 6})
            self.payload = {'userId': ListData["userId"], 'paySource': ListData["paySource"], 'list': ListData["list"]}
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            #self.testRecord.info(httper.url)
            #self.testRecord.info(httper.token)
            #self.testRecord.info(self.payload)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"] and res['data']['orderNo'] is not None:
                #self.testRecord.info(res)
                assert True
                self.orderNoInfo = res['data']
                try:
                    self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable2)
                    self.conn.runConn()
                    self.conn.insertData(self.orderNoInfo)
                except self.conn, e:
                    print "DB error", e

            else:
                #self.testRecord.info(res)
                assert False
        except self.conn, e:
            print "DB error", e

    def testCreateOrderByServer(self):
        """
        [createOrder] create order by Server
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 7})
            self.payload = {'userId': ListData["userId"], 'paySource': ListData["paySource"], 'list': ListData["list"]}
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            #self.testRecord.info(httper.url)
            #self.testRecord.info(httper.token)
            #self.testRecord.info(self.payload)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"] and res['data']['orderNo'] is not None:
                #self.testRecord.info(res)
                assert True
                self.orderNoInfo = res['data']
                try:
                    self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable2)
                    self.conn.runConn()
                    self.conn.insertData(self.orderNoInfo)
                except self.conn, e:
                    print "DB error", e
            else:
                #self.testRecord.info(res)
                assert False
        except self.conn,e:
            print "DB error",e

    def testCreateOrderByH5(self):
        """
        [createOrder] create order by H5
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 8})
            self.payload = {'userId': ListData["userId"], 'paySource': ListData["paySource"], 'list': ListData["list"]}
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            #self.testRecord.info(httper.url)
            #self.testRecord.info(httper.token)
            #self.testRecord.info(self.payload)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"] and res['data']['orderNo'] is not None:
                #self.testRecord.info(res)
                assert True
                self.orderNoInfo = res['data']
                try:
                    self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable2)
                    self.conn.runConn()
                    self.conn.insertData(self.orderNoInfo)
                except self.conn, e:
                    print "DB error", e
            else:
                #self.testRecord.info(res)
                assert False
        except self.conn,e:
            print "DB error", e