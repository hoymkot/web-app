# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from html import Html


urls = (
    '/wx', 'Handle',
    '/wechat/(.*)', 'Html',
)

class MyApplication(web.application):
    def run(self, port=80, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=80)

