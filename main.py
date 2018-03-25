import sys
from handlers.ArgumentHandler import ArgumentHandler


class Main:
    def __init__(self, args):
        self.arguments = args

    def run(self):
        handler = ArgumentHandler(self.arguments)
        commands = handler.parse()


if __name__ == "__main__":
    arguments = sys.argv
    mainObject = Main(arguments)
    mainObject.run()