class QueryWorker:
    def __init__(self, commands, iteration):
        self.name = __name__ + ':' + str(iteration)
        self.commands = commands
        self.issue = ''
        self.didWork = False

    def getName(self):
        return

    ##@todo aim should be for this to be a super method in child workers
    def run(self):

        if self.didWork:
            return True

        self.issue = 'Failed to connect'
        raise Exception(self.issue)