import re

class argumentHandler:

    buildTuple = ('workers', 'type', 'test')
    commandTuple = ('query', 'target')
    def __init__(self, inputArguments):
        self.arguments = inputArguments
        self.argWorkload = []
        self.buildRequests = []
        self.commandRequests = []

    def is_argument(self, stringTarget):
        if re.search('^--', stringTarget):
            return True
        return False

    def sort_build_and_command(self):
        for workload in self.argWorkload:
            paramAndValue = workload.split('=')
            if paramAndValue[0] in self.buildTuple:
                self.buildRequests.append({paramAndValue[0]: paramAndValue[1]})
                continue
            if paramAndValue[0] in self.commandTuple:
                self.commandRequests.append({paramAndValue[0]: paramAndValue[1]})
                continue
            raise Exception('argument: ' + paramAndValue[0] + ' not found in existing map')
        return False

    def parse(self):
        for argument in self.arguments:
            if self.is_argument(argument):
                self.argWorkload.append(argument[2:])

        if self.argWorkload.__len__() > 0:
            self.sort_build_and_command()

        if self.buildRequests and self.commandRequests:
             return {'buildRequests': self.buildRequests, 'commandRequests': self.commandRequests}

        raise Exception('argumentHandler unable to return full formatted '
                        'argument list due to build or command requests '
                        'being incomplete')