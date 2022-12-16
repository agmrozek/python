from unittest.mock import patch

...

class WhoTweetedTestCase(unittest.TestCase):

    @patch.object(tweepy.API, 'get_status', return_value=get_tweet('AU'))
    def test_julian(self, mock_method):
        ...

    @patch.object(tweepy.API, 'get_status', return_value=get_tweet('ES'))
    def test_bob(self, mock_method):
        ...