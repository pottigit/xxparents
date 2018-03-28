# -*- coding: utf-8 -*-

import requests
import hashlib
import json
import urllib
import urllib2
import nose


#建立基础http请求通信类
class HttpBase(object):
    #默认初始化方法，三个self参数（具体方法、请求地址、请求数据）
    def __init__(self, method, url, query, token):
        self.method = method
        self.url = url
        self.query = query
        self.token = token

    def httpRequest(self):
        if (self.method == 'GET'):
            try:
                #url = action if (query == None) else (action + '?' + query)
                connection = requests.get(self.url,
                                          params=self.query,
                                          headers={'Accept-Encoding': 'gzip',
                                                   'Authorization': 'Basic ' + self.token,
                                                   'Connection': 'keep-alive',
                                                   'Content-Type': 'application/json;charset=UTF-8',
                                                   'Host': '192.168.0.215:8084'}
                                          )
                res_get = json.loads(connection.text)
                return connection.status_code,res_get
            except requests.exceptions.HTTPError as e:
                return "error: " + str(e)


        elif (self.method == 'POST'):
            try:
                connection = requests.post(self.url,
                                            data = json.dumps(self.query),
                                            headers={   'Accept-Encoding': 'gzip',
                                                        'Authorization': 'Basic ' + self.token,
                                                        'Connection': 'keep-alive',
                                                        'Content-Type': 'application/json;charset=UTF-8',
                                                        'Host': '192.168.0.215:8084',
                                                        'User-Agent': 'okhttp/3.8.1'})
                res_post = json.loads(connection.text)
                #return connection.status_code,res_post
                return res_post
            except requests.exceptions.HTTPError as e:
                return "error: " + str(e)


        elif (self.method == 'POSTNOJSON'):
            try:
                #post_data = urllib.urlencode(query)

                req = urllib2.Request(self.url, self.query)
                #req.add_header('Accept', "application/x-www-form-urlencoded")
                req.add_header('Content-Type', "application/x-www-form-urlencoded")
                connection = urllib2.urlopen(req)

                #connection.encoding = "UTF-8"
                connection_result = json.loads(connection.read())
                return connection_result
            except requests.exceptions.HTTPError as e:
                return "error: " + str(e)
