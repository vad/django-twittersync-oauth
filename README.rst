CONFIGURING TWITTERSYNC_OAUTH
=============================

Set these in your settings.py (you can obtain consumer key and secret from
twitter.com)::

    TWITTER_APP_NAME = "Your App name"
    TWITTER_CONSUMER_SECRET = "####"
    TWITTER_CONSUMER_KEY = "####"
    

Add twittersync_oauth to your INSTALLED_APPS **after** twittersync::

    INSTALLED_APPS = (
        ...
        'twittersync',
        'twittersync_oauth',
        ...
    )
    

Then run::

    ./manage.py auth_twitter

auth_twitter opens a twitter authentication request in your browser. Please
note that you can do this on your own pc and then use the resulting keys on
your server. Click Accept and twitter gives you a PIN. Insert this PIN in the
manage.py you executed. The script gives you other two variables you need to
set in your settings.py. Done! :)