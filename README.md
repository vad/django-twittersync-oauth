CONFIGURING TWITTERSYNC_OAUTH
=============================
Set this variable in your settings.py:

    TWITTER_APP_NAME = "Your App name"
    TWITTER_CONSUMER_SECRET = "####"
    TWITTER_CONSUMER_KEY = "####"

Then add twittersync_oauth to your INSTALLED_APPS **under** twittersync:

    INSTALLED_APPS = (
        ...
        'twittersync',
        'twittersync_oauth',
        ...
    )

Where the SECRET and KEY are given to you by twitter. Then execute

    ./manage.py auth_twitter

this opens a twitter authentication request in your browser. Click Accept and
twitter gives you a PIN. Insert this PIN in the manage.py you executed. This
gives you other two variable to set in your settings.py. Done! :)