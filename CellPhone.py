#-*- coding: UTF-8 -*-
import json
import nose
from VerifyCodeBind import *
import logging
from logging.handlers import RotatingFileHandler
from ConnectMongoDB import *
from HttpBasePublic import *


class TestCellPhone():

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
        self.dbtable = "cell_phone"
        self.payload = {}
        self.token_dbtable = "public_token"

        api_url = "http://192.168.0.215:8084/api/parent/cellphone?"
        params_url = "os=android&osVersion=25&deviceBrand=OD103&appVersion=1.2.0&ip=10.0.1.43&lng&lat&deviceId=9ee0aeb206db182a&platform=1&appType=4&userno=1351111888800&timestamp="
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


    def testCellPhoneByFather(self):
        """
        [cellPhone] cell phone normally by father
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 1})

            self.payload = {'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'contactsRelation': ListData["contactsRelation"]}
            # 触发获取验证码动作
            touchSendCodeBind(ListData["loginNo"],ListData["phone"],self.token)
            time.sleep(1)
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False

        except self.conn,e:
            print "DB error", e

    def testCellPhoneByMonther(self):
        """
        [cellPhone] cell phone normally by mother
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 2})

            self.payload = {'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'contactsRelation': ListData["contactsRelation"]}
            # 触发获取验证码动作
            touchSendCodeBind(ListData["loginNo"],ListData["phone"],self.token)
            time.sleep(1)
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False

        except self.conn,e:
            print "DB error", e

    def testCellPhoneByOther(self):
        """
        [cellPhone] cell phone normally by other
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 3})

            self.payload = {'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'contactsRelation': ListData["contactsRelation"]}
            # 触发获取验证码动作
            touchSendCodeBind(ListData["loginNo"],ListData["phone"],self.token)
            time.sleep(1)
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False

        except self.conn,e:
            print "DB error", e

    def testCellPhoneNoContacts(self):
        """
        [cellPhone] cell phone without contacts
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 4})

            self.payload = {'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'contactsRelation': ListData["contactsRelation"]}
            # 触发获取验证码动作
            touchSendCodeBind(ListData["loginNo"],ListData["phone"],self.token)
            time.sleep(1)
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False

        except self.conn,e:
            print "DB error", e

    def testCellPhoneNoPhone(self):
        """
        [cellPhone] cell phone without phone
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 5})

            self.payload = {'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'contactsRelation': ListData["contactsRelation"]}
            # 触发获取验证码动作
            touchSendCodeBind(ListData["loginNo"],ListData["phone"],self.token)
            time.sleep(1)
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False

        except self.conn,e:
            print "DB error", e

    def testCellPhoneNoVerifyCode(self):
        """
        [cellPhone] cell phone without verifyCode
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 6})

            self.payload = {'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'contactsRelation': ListData["contactsRelation"]}
            # 触发获取验证码动作
            touchSendCodeBind(ListData["loginNo"],ListData["phone"],self.token)
            time.sleep(1)
            # 获得基础请求类对象
            httper = HttpBase('POST', self.url, self.payload, self.token)
            # 使用GET方法请求校区列表接口
            res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                #self.testRecord.info(res)
                assert True
            else:
                #self.testRecord.info(res)
                assert False

        except self.conn,e:
            print "DB error", e