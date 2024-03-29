# -*- coding: utf-8 -*-
# filename: basic.py
import urllib
import time
import json

class Basic:
    def __init__(self):
        self.__accessToken = ''
        self.__leftTime = 0
    def __real_get_access_token(self):
        appId = "wx90a8b2281428f6bd"
        appSecret = "b7e4694534eaf2af0641a566950803b0"
        #test account token
        #appId = "wx36d3575f12ca3ae4"
        #appSecret = "c2dac706309782f9af1f018aa090a3f0"
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))
        urlResp = urllib.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())		
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']
    def get_access_token(self):
        if self.__leftTime < 10:
            self.__real_get_access_token()
        return self.__accessToken
    def run(self):
        while(True):
            if self.__leftTime > 10:
                time.sleep(2)
                self.__leftTime -= 2
            else:
                self.__real_get_access_token()

if __name__ == '__main__':
    # 注意 URL 一定要动态获取，不能 hardcode
    b = Basic()
    print b.get_access_token()

