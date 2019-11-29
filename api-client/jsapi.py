# -*- coding: utf-8 -*-
# filename: basic.py
import urllib
import time
import json
from basic import Basic

class JsApi:
    def __init__(self, access_token):
        self.__accessToken = access_token
        self.__leftTime = 0
        self.__ticket = '';
    def __real_get_ticket(self):
        postUrl = ("https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=%s&type=jsapi" % (self.__accessToken.get_access_token()))
        urlResp = urllib.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())		
        self.__ticket = urlResp['ticket']
        self.__leftTime = urlResp['expires_in']
    def get_ticket(self):
        if self.__leftTime < 10:
            self.__real_get_ticket()
        return self.__ticket
    def run(self):
        while(True):
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_ticket()

if __name__ == '__main__':
    # 注意 URL 一定要动态获取，不能 hardcode
    b = Basic()
    api = JsApi(b)
    print api.get_ticket()

