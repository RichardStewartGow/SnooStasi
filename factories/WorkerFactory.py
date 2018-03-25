class WorkerFactory:

    workerTypeMap = {}
    classMap = {'query':'QueryWorker'}

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

        raise Exception('Worker Factory given no processable work')