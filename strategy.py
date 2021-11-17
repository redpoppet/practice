


class Model(object):
    pass


class Rebalance(Model):
    def __init__(self):
        pass 

    def run(self,args):
        print('run rebalance',args,sep=',')



class QuickResponse(Model):
    def __init__(self):
        pass 


    def run(self,args):
        print('run Quick response',args,sep=',')


class Classify(Model):
    def __init__(self):
        pass 

    def run(self,args):
        print('run Classify',args,sep=',')
    


class ModelMode:
    def __init__(self,model_instance):
        self.model_instance = model_instance

    
    def run(self,args):
        self.model_instance.run(args)
    
    

if __name__ == '__main__':
    args = 'test'
    model_instance1  = ModelMode(Rebalance())
    model_instance2  = ModelMode(Classify())
    model_instance1.run(args)
    model_instance2.run(args)

