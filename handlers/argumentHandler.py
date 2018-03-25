import re

class argumentHandler:

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
            if 'workers' in paramAndValue:
                self.buildRequests.append({'build': paramAndValue[1]})
                continue
            if 'type' in paramAndValue:
                self.buildRequests.append({'type': paramAndValue[1]})
                continue
        return False

    def parse(self):
        for argument in self.arguments:
            if self.is_argument(argument):
                self.argWorkload.append(argument[2:])

        if self.argWorkload.__len__() > 0:
            self.sort_build_and_command()

        return False