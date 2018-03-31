class BaseCommand:
    def __init__(self, praw, config):
        self.config = config
        self.praw = praw
