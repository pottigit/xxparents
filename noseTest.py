#-*- coding: utf-8 -*-
from ConnectMongoDB import *
from HttpBasePublic import *
import logging
from logging.handlers import RotatingFileHandler


class TestLogoConfig():

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
        self.dbdatabase = "doubleteacher"
        self.dbtable = "LogoConfig"
        self.paramsData = {}
        self.url = "http://xmpy.h5.fkls.com/parent/eb/logoConfig?"

    def tearDown(self):
        #self.testRecord.info("Logo config test is over")
        pass

    def testGetLogoConfigForXMPY(self):
        """
        get config for XMPY
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 1})

            #self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象

            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn,e:
            print "DB error",e



    def testGetLogoConfigForXMGX(self):
        """
        get config for XMGX
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 2})

            #self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn,e:
            print "DB error",e

    def testGetLogoConfigForXMCN(self):
        """
        get config for XMCN
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 3})

            #self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()

            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn,e:
            print "DB error",e

    def testGetLogoConfigForFZYS(self):
        """
        get config for FZYS
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 4})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForFZYK(self):
        """
        get config for FZYK
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 5})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForFZXX(self):
        """
        get config for FZXX
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 6})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForFZPY(self):
        """
        get config for FZPY
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 7})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForFZGX(self):
        """
        get config for FZGX
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 8})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForQZPY(self):
        """
        get config for QZPY
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 9})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForQZGX(self):
        """
        get config for QZGX
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 10})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForHFPY(self):
        """
        get config for HFPY
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 11})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            #self.testRecord.info(res)
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForHFGX(self):
        """
        get config for HFGX
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 12})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForNCYK(self):
        """
        get config for NCYK
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 13})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e

    def testGetLogoConfigForNCPY(self):
        """
        get config for NCPY
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 14})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForNCGX(self):
        """
        get config for NCGX
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 15})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForNCXX(self):
        """
        get config for NCXX
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 16})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e
    def testGetLogoConfigForJYZB(self):
        """
        get config for JYZB
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 17})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e

    def testGetLogoConfigForSHPY(self):
        """
        get config for SHPY
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 18})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e

    def testGetLogoConfigForSHGX(self):
        """
        get config for SHGX
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 19})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e

    def testGetLogoConfigForAKYX(self):
        """
        get config for AKYX
        :return:
        """
        try:
            self.conn = ConnectMongoDB(self.dbserver, self.dbport, self.dbdatabase, self.dbtable)
            self.conn.runConn()
            ListData = self.conn.findOneData({"caseId": 20})

            # self.paramsData['domain'] = ListData["domain"]
            # 获得基础请求类对象
            httper = HttpBase('GET', self.url, ListData["domain"])
            # 使用GET方法请求校区列表接口
            status_code, res = httper.httpRequest()
            if res['status'] == ListData["response"]:
                assert True
                #self.testRecord.info(ListData["caseType"])
            else:
                assert False
                #self.testRecord.info(ListData["caseType"])

        except self.conn, e:
            print "DB error", e