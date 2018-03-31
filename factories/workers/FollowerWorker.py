from .BasicWorker import BasicWorker


class FollowerWorker(BasicWorker):
    def __init__(self):
        super.__init__()

    def check_commands_valid(self):
        for command in self.commands:
            continue

    def run(self):
        super.run()

        if self.didWork:
            return True

        if not self.check_commands_valid():
            raise Exception('Commands given to ' + __name__  + ' invalid')

