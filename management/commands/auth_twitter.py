from django.conf import settings
from django.core.management.base import NoArgsCommand
from twitter.oauth_dance import oauth_dance

class Command(NoArgsCommand):
    help = 'Returns OAuth Token.'

    def handle_noargs(self, **options):
        oauth_token, oauth_token_secret = oauth_dance(
            settings.TWITTER_APP_NAME,
            settings.TWITTER_CONSUMER_KEY,
            settings.TWITTER_CONSUMER_SECRET
        )

        print 'TWITTER_TOKEN =', oauth_token
        print 'TWITTER_TOKEN_SECRET =', oauth_token_secret