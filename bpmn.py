from bpmn_dmn.bpmn import BPMNXMLWorkflowRunner

class Lorder:
    def __init__(self, status, printedfl):
        self.status = status
        self.printedfl = printedfl

runner = BPMNXMLWorkflowRunner('exclusive_gateway_two_if_else.bpmn', debug=True)
runner.start(lorder=Lorder(2, True))
res = runner.getEndEventName()
print(res)
