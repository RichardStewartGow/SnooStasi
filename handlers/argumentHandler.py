import re

class argumentHandler:

    def __init__(self, inputArguments):
        self.arguments = inputArguments
        self.argWorkload = []

    def is_argument(self, stringTarget):
        if re.search('^--', stringTarget):
            return True
        return False

    def sort_build_and_command(self):
        return False

    def parse(self):
        for argument in self.arguments:
            if self.is_argument(argument):
                self.argWorkload.append(argument[2:])

        return False