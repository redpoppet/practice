class Manager(object):
    successor = None
    name = ''

    def __init__(self,name):
        self.name=name 

    def setSuccessor(self,successor):
        self.successor = successor

    
    def handleRequest(self,request):
        pass 

class LineManager(Manager):
    def handleRequest(self, request):
        if request.request_type == 'DaysOff'  and request.number <=3:
            print('accept')
        else:
            print('accept continue')
            if self.successor:
                self.successor.handleRequest(request)
    

class DepartManager(Manager):
    def handleRequest(self, request):
        if request.request_type == 'DaysOff' and request.number <=7:
            print('accept')
        else:
            print('accept continue')
            if self.successor:
                self.successor.handleRequest(request)

class GenenalManage(Manager):
    def handleRequest(self, request):
        if request.request_type == 'DaysOff':
            print('accept')

    

class Request():
    request_type = ''
    request_content = ''
    number = 0


if __name__ == "__main__":

    Line_manage = LineManager('line manager')
    department_manager = DepartManager('department manager')
    general_manager = GenenalManage('general manager')
    
    Line_manage.setSuccessor(department_manager)
    department_manager.setSuccessor(general_manager)

    req = Request()
    req.request_type='DaysOff'
    req.request_content = 'ask 2 day fro '
    req.number = 1

    Line_manage.handleRequest(req)

