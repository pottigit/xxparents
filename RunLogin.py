#-*- coding: UTF-8 -*-
import os
import logging
from logging.handlers import RotatingFileHandler
from ConnectMongoDB import *
from HttpBasePublic import *
from ParentsLogin import *
import qaklssparents.ParentsLogin

class RunLogin():

    def __init__(self):
        self.init_logging()
        self.path = './xxparents'
        self.info_index = 1
        self.token_index = 0

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

    def LoginParents(self, user_type):

        loginStatus = getToken(self.path, self.info_index, self.token_index, user_type)

        if loginStatus is True:
            self.testRecord.info(" %s user login successfully" % user_type)
        else:
            self.testRecord.info("login failed and pls check error")

if __name__=='__main__':
    clearToken('./xxparents', 0)
    userType = ['operateValidData','operateInvalidData']
    for item in userType:

        RunLogin().LoginParents(item)
        time.sleep(2)
