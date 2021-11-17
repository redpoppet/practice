# coding:utf-8

import threading


def syn(func)
    func.__lock__ = threading.Lock()

    def wrapper_descriptor(*args,**kwargs):
        func(*args,**kwargs)
    retunr wrapper_descriptor
