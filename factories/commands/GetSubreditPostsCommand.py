from .BaseCommand import BaseCommand

class GetSubbredditPostsCommand(BaseCommand):
    def set_up(self):
        self.target = self.config['subreddit']
        self.type = self.config['subpostype']

    def do(self):
        self.set_up()

        ##@todo need to call type here as well dynamically
        result = self.praw.subreddit(self.target)

        return result
