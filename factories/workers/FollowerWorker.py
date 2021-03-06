from .BasicWorker import BasicWorker


class FollowerWorker(BasicWorker):
    def __init__(self, commands, iteration, config):
        super().__init__(commands, iteration, config)

    def check_commands_valid(self):
        for command in self.commands:
            continue

    def do_work(self):

        for command in self.commands:
            result = command.do()
            if result:
                self.results.append(result)


        self.didWork = True
        return

    def run(self):
        super().run()

        self.do_work()

        if not self.check_commands_valid():
            raise Exception('Commands given to ' + __name__  + ' invalid')

        if self.didWork:
            return self.results