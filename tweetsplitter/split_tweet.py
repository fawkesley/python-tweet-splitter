from __future__ import unicode_literals


def split_tweet(long_tweet, length=140):
    assert length >= 10

    if len(long_tweet) <= length:
        return [long_tweet]

    words = long_tweet.split(' ')

    return list(_split_tweets(words, length))


def _split_tweets(words, length):
    tweets = list(_generate_split_tweets(words, length))
    assert len(tweets) < 10

    for i, tweet in enumerate(tweets):
        yield '{}/{}{}'.format(i + 1, len(tweets), tweet[3:])


def _generate_split_tweets(words, length):
    this_tweet = '?/?'

    while True:
        this_tweet += ' ' + words.pop(0)

        if not words:
            break

        if len(this_tweet) + 1 + len(words[0]) > length:
            yield this_tweet
            this_tweet = '?/?'

    yield this_tweet
