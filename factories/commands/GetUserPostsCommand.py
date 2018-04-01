from .BaseCommand import BaseCommand


class GetUserPostsCommand(BaseCommand):
    def __init__(self, praw, commands):
        super().__init__(praw, commands)

    def set_up(self):
        self.target = self.config['target']

    def do(self):
        self.set_up()

        result = self.praw.get_redditor(self.target)

        return result
