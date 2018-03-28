#-*- coding: UTF-8 -*-
import json
import nose
from VerifyCode import *
import logging
from logging.handlers import RotatingFileHandler
from ConnectMongoDB import *
from HttpBasePublic import *


class TestAddCart():

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
        self.dbtable = "resetPassword"
        self.payload = {}
        self.token_dbtable = "public_token"

        api_url = "http://192.168.0.215:8084/api/parent/password/reset?"
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


    def testresetPasswordNumber(self):
        """
        [resetPassword] reset password which 6 bit number normally
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 1})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

    def testresetPasswordCharacter(self):
        """
        [resetPassword] reset password which 6 bit character normally
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 2})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

    def testresetPasswordMixed(self):
        """
        [resetPassword] reset password which mixed character normally
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 3})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

    def testresetPassword20bitMixed(self):
        """
        [resetPassword] reset password which 20 bit mixed character normally
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 4})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

    def testresetPasswordAbove20bit(self):
        """
        [resetPassword] reset password above 20 bit
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 5})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

    def testresetPasswordLess5bit(self):
        """
        [resetPassword] reset password less than 6 bit
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 6})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

    def testresetPasswordNoVerifyCode(self):
        """
        [resetPassword] reset password but not input verifyCode
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 7})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

    def testresetPasswordNoLoginNo(self):
        """
        [resetPassword] reset password but not input loginNo
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 8})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

    def testresetPasswordNoLoginNo(self):
        """
        [resetPassword] reset password but not input loginNo
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 9})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

    def testresetPasswordNoPassword(self):
        """
        [resetPassword] reset password but not input password
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 10})

            self.payload = {'loginNo': ListData["loginNo"],
                            'phone': ListData["phone"],
                            'verifyCode': ListData["verifyCode"],
                            'password': ListData["password"]}
            # 触发获取验证码动作
            touchSendCode(ListData["loginNo"],ListData["phone"],self.token)
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

        except self.conn, e:
            print "DB error", e