class Singleton(type):
    def __init__(self):
        self._instance=None
        super().__init__(*args,**kwargs)
    
    def __call__(self,*args,**kwargs):
        if self._instance is None:
            self.__instance = super().__call__(*args,**kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('Createing Spam')



