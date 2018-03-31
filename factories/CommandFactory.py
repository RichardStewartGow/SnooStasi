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
            ##@todo figure out why this isunt working in this context - depth?
            classObject = classObject = getattr(moduleObject, className)(
                praw, commands
            )

        return


