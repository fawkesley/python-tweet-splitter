from nose.tools import assert_equal, assert_less_equal

from . import split_tweet

_TESTS = [
    ("I'm not sure what to do", 23, ["I'm not sure what to do"]),
    ("I'm not sure what to do", 22, ["1/2 I'm not sure what", "2/2 to do"]),
    ("I'm not sure what to do", 21, ["1/2 I'm not sure what", "2/2 to do"]),
    ("I'm not sure what to do", 20, ["1/2 I'm not sure", "2/2 what to do"]),
]

_TEST_SENTENCE = 'The quick brown fox jumps over the lazy dog'


def test_every_length():
    for length in range(len(_TEST_SENTENCE), 10, -1):
        yield _do_test_split_sanity, _TEST_SENTENCE, length


def _do_test_split_sanity(text, length):
    tweets = split_tweet(text, length)
    for tweet in tweets:
        assert_equal(tweet.strip(' '), tweet)  # no whitespace
        assert_less_equal(len(tweet), length)  # not too long


def test_known_examples():
    for original, length, expected in _TESTS:
        yield _do_test_split, original, length, expected


def _do_test_split(text, length, expected_splits):
    got = split_tweet(text, length)
    assert_equal(expected_splits, got)
