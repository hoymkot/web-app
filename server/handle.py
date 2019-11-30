# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "hello" #请按照公众平台官网\基本配置中信息填写

            l = [token, timestamp, nonce]                       
            l.sort()
            hashcode = self.hashgen(l);
            print ("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            return Argument

    def hashgen(object, t):
        print(t)
        sha1 = hashlib.sha1()
        map(sha1.update, t);
        code = sha1.hexdigest();
        print(code);
        return code;


    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = "test"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                if isinstance(recMsg, receive.EventMsg):
                    if recMsg.Event == 'CLICK':
                        if recMsg.Eventkey == 'jidai_location':         
                            
                            #replyMsg = reply.TextMsg(toUser, fromUser, 
                            #"广隆吉大店\n0756-3228782\n珠海市香洲区\n吉大石花东路203号"
                            #)
                        if recMsg.Eventkey == 'jinji_location':                            
                            replyMsg = reply.TextMsg(toUser, fromUser, 
                            "广隆前山店\n0756-8652111\n珠海市香洲区\n前山金鸡路路555号"
                            )
                        return replyMsg.send()
            else:
                print ("暂且不处理")
                return "success"
        except Exception as Argment:
            return Argment
