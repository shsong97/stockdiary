import tweepy
# http://tweepy.readthedocs.org/en/v3.2.0/getting_started.html
consumer_key='EAeYEFYmUvVQVcHRfv9yEg'
consumer_secret='6SdVrmXMpz9T7kik7s3JBbsLR9LJtwqY0IWMIkqNDA'
access_token='132161704-fJrB2l7sTWeoIuWoRTyMJIIMgRNmXtwRijdB7aDZ'
access_token_secret='rXluxL6ec37575JzZQ0nFVTgFBS35jrnmXONmCeA1U25z'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)