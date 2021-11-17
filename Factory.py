#encoding:utf-8

import logging 
import logging.config
from utils import init_log
from utils import ContextFilter

init_log()

logger = logging.getLogger(__name__)
logger.addFilter(ContextFilter())

class Car(object):
    def run(self):
        print('xxx run')
    
    def stop(self):
        print('xxx stop')

class BMW(Car):
    def run(self):
        print('bmw run')
    
    def stop(self):
        print('bmw stop')
    

class Benz(Car):
    def run(self):
        print('benz run')
    
    def stop(self):
        print('Bnez run')



class CarFactory(object):
    def new_car(self,name):
        if name=='bmw':
            bmw = BMW()
            return bmw 
        elif name=='Benz':
            benz = Benz()
            return benz
        else:

            raise NotImplemented


class CarStore(object):
    def __init__(self,factory):
        self.factory = factory

    def order(self,name):
        new_car = self.factory.new_car(name)
        return new_car


class Sun(object):
    instance = None

    def __new__(cls,*args,**kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            return cls.instance
        else:
            return cls.instance



from test import test 


if __name__ == "__main__":
    from pathlib import Path
    basedir = Path(__file__).resolve().parents[0]
    logger.error('this is a test error')
    car_factory = CarFactory()
    car_store = CarStore(car_factory)
    car = car_store.order('Benz')
    car.run()
    car.stop()
    test()




