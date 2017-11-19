# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 00:02:08 2017

@author: admin
"""

from tornado.curl_httpclient import CurlAsyncHTTPClient
from tornado import gen
from tornado.ioloop import IOLoop

class ProxyPool(object):
    IPs=[]
    def __init__(self,timelastupdate):
        self.timelastupdate=timelastupdate
    def getIPs(self):
        pass
    def checkIP(self):
        pass
    def write2DB(self):
        pass
    def write2conf(self):
        pass
    def readfromDB(self):
        pass
    
@gen.coroutine


