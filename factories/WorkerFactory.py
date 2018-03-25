class WorkerFactory:

    workerTypeMap = {}
    classMap = {'query':'QueryWorker'}

    def __init__(self, commands):
        self.commands = commands
        self.set_up_commands()

    def set_up_commands(self):
        return True;

    def build(self):
        for command in self.commands:
            return True

        raise Exception('Worker Factory given no processable work')