#-*- coding : utf-8 -*-
import json
from ConnectMongoDB import *
from ReadDBConfig import *

def mongoConnByConfig(file_path, file_index):
    try:
        dbserver, dbport, dbdatabase, dbtable = ReadMongo(file_path, file_index).getMongoData()
        conn = ConnectMongoDB(dbserver, dbport, dbdatabase, dbtable)
        runner = conn.runConn()
        return runner

    except conn,e:
        print "DB error", e



def mongoConnByInput(dbserver,dbport,dbdatabase,dbtable):
    try:
        conn = ConnectMongoDB(dbserver, dbport, dbdatabase, dbtable)
        runner = conn.runConn()
        return runner

    except conn, e:
        print "DB error", e
