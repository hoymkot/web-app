# -*- coding: utf-8 -*-
# filename: handle.py

import web
import reply
import receive


class Html(object):
    def GET(self, action):
        try:
            render = web.template.frender('templates/'+action)
            return render();
        except Exception as Argument:
            return Argument


    def POST(self):
        try:
            return 'POST'
        except Exception as Argment:
            return Argment
