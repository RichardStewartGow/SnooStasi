#@todo refactor into class into own file

import sys
from handlers import argumentHandler

class main:
    def __init__(self, arguments):
        self.arguments = arguments
        return #@todo stub for now do more setup logic here
    def run(self):
        processes = argumentHandler(arguments)

if __name__ == "__main__":
    arguments = sys.argv
    mainObject = main(arguments)
    main.run