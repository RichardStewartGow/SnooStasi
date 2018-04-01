from .commands import GetSubreditPostsCommand, GetUserPostsCommand
import sys


class CommandFactory:

    prawTranslaslationMap = {
        'follow-user': 'target',
        'follow-subreddit': 'subreddit',
        'rank-by': 'subposttype'
    }
    classMap = {
        'follow-user': 'GetUserPostsCommand',
        'follow-subreddit': 'GetSubredditPostsCommand'
    }

    def build(self, praw, commands):

        for command in commands:
            className = self.classMap[command]
            moduleObject = getattr(sys.modules[__name__], className)
            classObject = getattr(moduleObject, className)(
                praw, commands
            )

        return classObject


