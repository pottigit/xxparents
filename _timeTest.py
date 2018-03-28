#-*- coding: UTF-8 -*-
import os
import sys
import json
import nose
import time

def runTime():

    dt = "2018-01-17 14:16:24"

    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)

    print timestamp
    print int(round(timestamp * 1000))


    thrityTime = int(round(time.time() * 1000))
    print type(str(thrityTime))
    print thrityTime

def strTest():
    http_query = {"loginNo": "1386666111100",
                  "password": "111100"}

    s1 = http_query.get("loginNo")
    print s1

strTest()