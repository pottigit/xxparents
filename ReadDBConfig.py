#-*- coding : utf-8 -*-

import os
import sys
import json

class ReadMongo(object):

    def __init__(self,dbfile_name,db_index):
        self.dbfile_name = dbfile_name
        self.db_index = db_index
        #self.table_asname = table_asname


    def getMongoData(self):
        try:
            df = open(self.dbfile_name,'r')
            db_data = json.load(df)
            #print db_data
            if db_data['datainfo'][self.db_index]['id'] == self.db_index:

                return db_data['server'], db_data['port'],\
                       db_data['database'], db_data['datainfo'][self.db_index]['table']

            else:
                print "nothing"
        except IOError, e:
            print "error is about : ", e


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

    path = './klxxparents'
    index = 1
    read_handler = ReadMongo(path,index)
    table = read_handler.getMongoData()
    print table
    print type(table)


