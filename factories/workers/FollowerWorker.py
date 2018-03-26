import QueryWorker


class FollowerWorker(QueryWorker):
    def __init__(self):
        super.__init__()

    def check_commands_valid(self):
        for command in self.commands:
            continue

    def run(self):
        super.run()

        if not self.check_commands_valid():
            raise Exception('Commands given to ' + __name__  + ' invalid')

