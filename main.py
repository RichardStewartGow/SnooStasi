#@todo refactor into class into own file

import sys
from handlers.argumentHandler import argumentHandler

class main:
    def __init__(self, args):
        self.arguments = args
    def run(self):
        handler = argumentHandler(self.arguments)
        commands = handler.parse()

if __name__ == "__main__":
    arguments = sys.argv
    mainObject = main(arguments)
    mainObject.run()