import sys
from os.path import basename

from .split_tweet import split_tweet


def main():
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} "<very long tweet>"\n'.format(
            basename(sys.argv[0])))
        sys.exit(2)

    for tweet in split_tweet(sys.argv[1]):
        sys.stdout.write('{}\n'.format(tweet))
