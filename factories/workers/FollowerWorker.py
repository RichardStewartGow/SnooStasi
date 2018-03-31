from .BasicWorker import BasicWorker


class FollowerWorker(BasicWorker):
    def __init__(self):
        super.__init__()

    def check_commands_valid(self):
        for command in self.commands:
            continue

    def do_work(self):

        for command in self.commands:
            result = command.do()
            if result:
                self.results.append(result)


        self.didWork = True
        return;

    def run(self):
        super.run()

        self.do_work()

        if self.didWork:
            return True

        if not self.check_commands_valid():
            raise Exception('Commands given to ' + __name__  + ' invalid')

