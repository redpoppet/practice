import weakref
class Cached(type):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__cache = weakref.WeakKeyDictionary()
    
    def __call__(self,*args,**kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj 
            return obj
        
class Spam(metaclass=Cached):
    def __init__(self,name):
        print("Creating Spam({!r})").format(name)
        self.name=name 
        