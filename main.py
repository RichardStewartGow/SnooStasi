import sys, yaml
from handlers.ArgumentHandler import ArgumentHandler
from factories.WorkerFactory import WorkerFactory


class Main:
    def __init__(self, args):
        self.arguments = args

    def get_config(self):

        with open('config/config.yml', 'r') as stream:
            try:
                yamlContents = yaml.load(stream)
                return yamlContents
            except:
                raise Exception('Issue opening config/config.yml file')


    def run(self):
        handler = ArgumentHandler(self.arguments)
        requests = handler.parse()
        requests['config'] = self.get_config()
        workerFactory = WorkerFactory(requests)
        workersBracket = workerFactory.build()
        workersBracket.run_workers()


if __name__ == "__main__":
    arguments = sys.argv
    mainObject = Main(arguments)
    mainObject.run()