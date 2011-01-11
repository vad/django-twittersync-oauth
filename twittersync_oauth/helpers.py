from twittersync.models import TwitterStatus
from twittersync.helpers import TwitterSyncHelper
from twitter import TwitterHTTPError
import logging

class TwitterSyncOAuthHelper(TwitterSyncHelper):
    def __init__(self, account, connection):
        super(TwitterSyncOAuthHelper, self).__init__(account)
        self.conn = connection

    def sync_twitter_account(self):
        # If previous updates exist, only get newer tweets
        try:
            latest = self.account.tweets.latest()
        except TwitterStatus.DoesNotExist:
            latest = None

        params = {
            'screen_name': self.account.screen_name,
            'trim_user': 't'
        }

        if latest is not None:
            params['since_id'] = latest.status_id

        try:
            results = self.conn.statuses.user_timeline(**params)
        except TwitterHTTPError, e:
            logging.warning('MainTwitterSyncHelper: connection error',
                            params['screen_name'])
            # Twitter often gives 503 errors when the
            # API is overwhelmed.
            pass
        else:
            for result in results:
                self.save_status_update(result)