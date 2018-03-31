from .BaseCommand import BaseCommand


class GetUsersPostsCommand(BaseCommand):

    def set_up(self):
        self.target = self.config['target']

    def do(self):
        self.set_up()

        result = self.praw.get_redditor(self.target)

        return result
