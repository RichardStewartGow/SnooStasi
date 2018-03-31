from .commands import GetSubreditPostsCommand, GetUserPostsCommand
import sys

class CommandFactory:

    classMap = {
        'follow-user': 'GetUserPostsCommand',
        'follow-subreddit': 'GetSubredditPostsCommand'
    }

    def build(self, praw, commands):

        for command in commands:
            className = self.classMap[command]
            moduleObject = getattr(sys.modules[__name__], className)
            classObject = classObject = getattr(moduleObject, className)(
                praw, commands
            )

        return


