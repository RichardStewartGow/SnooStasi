import praw

class BasicWorker:
    def __init__(self, commands, iteration, config):
        self.name = __name__ + ':' + str(iteration)
        self.commands = commands
        self.config = config
        self.issue = ''
        self.results = []
        self.didWork = False
        self.reddit = None

    def getName(self):
        return self.name

    def getIssue(self):
        return self.issue

    def set_up_praw(self):
        try:
            self.reddit = praw.Reddit(
                client_id=self.config['redditScript']['key'],
                client_secret=self.config['redditScript']['secret'],
                password=self.config['redditScript']['password'],
                user_agent='SnooStasi.a.1',
                username=self.config['redditScript']['username']
            )
        except Exception as error:
            self.issue = error.args[0]
            return False

        return True

    ##@todo aim should be for this to be a super method in child workers
    def run(self):

        if self.set_up_praw():
            return True

        self.issue = 'Failed to connect'
        raise Exception(self.issue)