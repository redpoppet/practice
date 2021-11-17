from threading import Lock

def syn(fun):
    fun.__lock__ = Lock()
    def wrapper_descriptor(*args,**kwargs):
        fun(*args,**kwargs)
    return wrapper_descriptor


class singleton(object):
    instance = None 

    @syn
    def __new__(cls):
        if cls.instance is not None:
            cls.instance = super(singleton,cls).__new__()
        return cls.instance
