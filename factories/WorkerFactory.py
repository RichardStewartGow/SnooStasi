from .workers import QueryWorker, WorkerBracket
import sys

class WorkerFactory:

    workerTypeMap = {}
    classMap = {'spy':'QueryWorker'}

    def __init__(self, requests):
        self.requests = requests
        self.buildCounter = 0
        self.buildLogic = {}
        self.validate_requests()

    def validate_requests(self): #@todo more validation here
        if 'buildRequests' not in self.requests and'commandRequests' not in self.requests:
            raise Exception('Factory not given list of build and command requests')

        return True

    def build(self):
        self.buildCounter = self.requests['buildRequests']['workers']

        workerHoldingArray = []

        ##@todo look into refactoring below to take out classname as is being instanciated mutliple times
        for counter in range(int(self.buildCounter)):
            className = self.classMap[self.requests['buildRequests']['type']]
            moduleObject = getattr(sys.modules[__name__], className)
            classObject = getattr(moduleObject, className)(self.requests['commandRequests'])
            workerHoldingArray.append(classObject)

        raise Exception('Worker Factory given no processable work')