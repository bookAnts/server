# coding: UTF-8

from base import BaseHandler

class Login(BaseHandler):
    def get(self):
        self.write("It works!")