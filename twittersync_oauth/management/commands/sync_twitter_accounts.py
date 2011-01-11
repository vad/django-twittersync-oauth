from django.conf import settings
from django.core.management.base import NoArgsCommand
from twittersync.models import TwitterAccount
from twittersync_oauth.helpers import TwitterSyncOAuthHelper
from twitter import Twitter, OAuth


class Command(NoArgsCommand):
    help = 'Sync all active Twitter account streams.'

    def handle_noargs(self, **options):
        conn = Twitter(domain="api.twitter.com", api_version='1',
                       auth=OAuth(settings.TWITTER_TOKEN,
                                  settings.TWITTER_TOKEN_SECRET,
                                  settings.TWITTER_CONSUMER_KEY,
                                  settings.TWITTER_CONSUMER_SECRET
                                  )
                       )
        for account in TwitterAccount.active.all():
            TwitterSyncOAuthHelper(account, conn).sync_twitter_account()
