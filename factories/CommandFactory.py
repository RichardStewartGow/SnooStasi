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

        ##@todo may be more appropriate to give this a bracket, unsure
        ##atm how running mutliple commands in sequence needs to work
        outputArray = []

        for command in commands:
            className = self.classMap[command]
            moduleObject = getattr(sys.modules[__name__], className)
            classObject = getattr(moduleObject, className)(
                praw, commands
            )

            outputArray.append(classObject)



        return outputArray


