import praw

class QueryWorker:
    def __init__(self, commands, iteration, config):
        self.name = __name__ + ':' + str(iteration)
        self.commands = commands
        self.config = config
        self.issue = ''
        self.didWork = False
        self.reddit = None

    def getName(self):
        return self.name

    def getIssue(self):
        return self.issue

    def set_up_praw(self):
        try:
            test = 'test'
            self.reddit = praw.Reddit(
                client_id=self.config['reddit']['key'],
                client_secret=self.config['reddit']['secret'],
                password=self.config['reddit']['password'],
                user_agent='test',
                username=self.config['reddit']['username']
            )

            self.reddit.user.me();
        except Exception:
            return Exception

        return True

    ##@todo aim should be for this to be a super method in child workers
    def run(self):

        self.set_up_praw()

        if self.didWork:
            return True


        self.issue = 'Failed to connect'
        raise Exception(self.issue)