#-*- coding : utf-8 -*-

import os
import sys
import json
import klssparents.ConnectMongoDB as CMDB

class ReadConfig(object):

    def __init__(self,urlfile_name,platform,dbfile_name,db_index):
        self.urlfile_name = urlfile_name
        self.platform = platform
        self.dbfile_name = dbfile_name
        self.db_index = db_index
        conner = CMDB()

    def getPlatformUrl(self):
        try:
            pf = open(self.urlfile_name,'r')
            url_data = json.load(pf)
            if url_data['platformInfo'][0]['platform'] == self.platform:

                return url_data['platformInfo'][0]['Url']

            if url_data['platformInfo'][1]['platform'] == self.platform:

                return url_data['platformInfo'][1]['Url']

            if url_data['platformInfo'][2]['platform'] == self.platform:

                return url_data['platformInfo'][2]['Url']
        except IOError,e:
            print "error is about : ",e





if __name__=='__main__':
    path = './url_config'
    parmaters = "test"
    url = ReadConfig(path,parmaters).getPlatformUrl()
    print url
    print type(url)

