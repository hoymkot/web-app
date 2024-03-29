import time
import random
import string
import hashlib
from jsapi import JsApi
from basic import Basic

class Sign:
    def __init__(self, jsapi_ticket, url):
        self.ret = {
            'nonceStr': self.__create_nonce_str(),
            'jsapi_ticket': jsapi_ticket,
            'timestamp': self.__create_timestamp(),
            'url': url
        }

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def sign(self):
        string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
        print string
        self.ret['signature'] = hashlib.sha1(string).hexdigest()
        return self.ret

if __name__ == '__main__':
    b = Basic()
    api = JsApi(b)
    ticket= api.get_ticket()
    sign = Sign(ticket, 'http://54.241.187.189/wechat/sandbox.html')
    print sign.sign()
