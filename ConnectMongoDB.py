#-*- coding : utf-8 -*-
import os
import sys
import nose
import pymongo as pm
from _csv import Error


class ConnectMongoDB(object):
    def __init__(self,host,port,db_name,collection):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection = collection

    def runConn(self):
        '''self.host = host
        self.port = port
        try:
            self.conn = pymongo.collection(self.host,self.port)
        except Error:
            print "connect to %s:%s fail" % (self.host,self.port)
        '''
        # create db conn
        try:
            self.client = pm.MongoClient(self.host, self.port)
            # db name
            self.db = self.client.get_database(self.db_name)
            # print self.db
            # set collection
            self.conn = self.db.get_collection(self.collection)
            # print self.coll
            print "conn DB successfully"
        except Exception,e:
            print "conn DB error,pls check DB",e

    def insertData(self,data=None):
        if data == None:
            self.conn.insert()
            print "insert successfully"
        else:
            self.conn.insert_one(data)
            print "insert data successfully"

    def updateData(self,data,expression=None):
        if expression == None:
            self.conn.update(data)
            print "update data successfully"
        else:
            self.conn.update( expression,{ "$set" : {data} } )
            print "update data successfully"

    def findMoreData(self, expression=None):

        if expression == None:
            return self.conn.find()
        else:
            return self.conn.find(expression)


    def findOneData(self, expression=None):
        if expression == None:
            return self.conn.find_one()
        else:
            return self.conn.find_one(expression)
    def deleteData(self, expression=None):
        if expression == None:
            self.conn.remove()
        else:
            self.conn.remove(expression)
    def close(self):
        self.conn.close()
