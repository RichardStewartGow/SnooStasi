import sys
from handlers.ArgumentHandler import ArgumentHandler
from factories.WorkerFactory import WorkerFactory


class Main:
    def __init__(self, args):
        self.arguments = args

    def run(self):
        handler = ArgumentHandler(self.arguments)
        requests = handler.parse()
        workerFactory = WorkerFactory(requests)
        workersBracket = workerFactory.build()
        workersBracket.run_workers()


if __name__ == "__main__":
    arguments = sys.argv
    mainObject = Main(arguments)
    mainObject.run()