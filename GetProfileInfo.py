#-*- coding: utf-8 -*-
import os
import sys
import json
import time
import logging
from logging.handlers import RotatingFileHandler
from ConnectMongoDB import *
from HttpBasePublic import *


class TestCartList():

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
        self.dbtable = "profile_info"
        self.payload = {}
        self.token_dbtable = "public_token"

        api_url = "http://192.168.0.215:8084/api/parent/profile?"
        params_url = "os=android&osVersion=25&deviceBrand=OD103&appVersion=1.2.0&ip=10.0.1.43&lng&lat&deviceId=9ee0aeb206db182a&platform=1&appType=4&timestamp="
        times = str(int(round(time.time() * 1000)))
        self.url = api_url + params_url + times

        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.token_dbtable)
            self.conn.runConn()
            dic_token = self.conn.findOneData({"userId":"1351111888800"})
            self.token = dic_token['ptoken']

        except self.conn, e:
            print "DB error", e

    def tearDown(self):
        #self.testRecord.info("Logo config test is over")
        pass

    def testGetProfileInfo(self):
        """
        [GetProfileInfo] get profile info of 1381111888800
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 1})

            self.payload = {'userNo': ListData["userNo"]}
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, self.payload, self.token)
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                self.testRecord.info(res['data']['children'])
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn,e:
            print "DB error",e

    def testGetProfileInfoNoUserno(self):
        """
        [GetProfileInfo] get profile info without userNo
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 2})
            self.payload = {'userNo': ListData["userNo"]}
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, self.payload,self.token)
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                self.testRecord.info(res['data']['children'])
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn,e:
            print "DB error",e