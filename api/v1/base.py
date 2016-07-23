# coding: UTF-8

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self,application,request,**kwargs):
        tornado.web.RequestHandler.__init__(self,application,request,**kwargs)
