#-*- coding : utf-8 -*-
import os
import sys
import json
import nose
import time
from ReadDBConfig import *
from ConnectMongoDB import *
from HttpBasePublic import *

def test2(p,i,urladdress):
    handle1 = ReadMongo(p,i)
    result = handle1.getMongoData()
    server_ip = result[0]
    port = result[1]
    databases = result[2]
    table = result[3]
    print "db server ip :",server_ip
    print "db server port : ",port
    print "db server databases : ",databases
    print "db server table :",table

    conner = ConnectMongoDB(server_ip,port,databases,table)
    conner.runConn()
    more_data = conner.findMoreData()
    http_params = {}
    for http_query in more_data:
        print http_query
        http_params['loginNo'] = http_query['loginNo']
        http_params['password'] = http_query['password']
        httper = HttpBase()
        responseer = httper.httpRequest('POST',urladdress,http_params)
        print responseer['message']

if __name__=='__main__':
    # index : 0,table : parentsLogin,asname : pl
    # index : 1,table : LoginConfig,asname : lc
    # index : 2,table : branchListData,asname : bld
    # index : 3,table : addCart,asname : ac
    # index : 4,table : deleteCart,asname : dc
    # index : 5,table : deleteInvalidCart,asname : dic
    # index : 6,table : cartList,asname : cl
    # index : 7,table : checkCart,asname : cc
    # index : 8,table : checkUser,asname : cu
    # index : 9,table : createOrder,asname : co
    # index :10,table : confirmOrder,asname : cfo
    # index :11,table : orderList,asname : ol
    # index :12,table : orderDetail,asname : od
    # index :13,table : updateOrder,asname : upo
    # index :14,table : queryVaildPeoples,asname : qvp
    # index :15,table : couponDetail,asname : cd
    # index :16,table : courseCouponList,asname : ccl
    # index :17,table : activityDetail,asname : ad
    http_url = 'http://192.168.0.215:8084/api/parent/login?'
    path = './klxxparents'
    index = 0

    test2(path,index,http_url)
