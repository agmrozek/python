from unittest.mock import patch

@patch.object(facebook.GraphAPI, 'put_object', autospec=True)
def test_post_message(self, mock_put_object):
    sf = simple_facebook.SimpleFacebook("fake oauth token")
    sf.post_message("Hello World!")
    mock_put_object.assert_called_with(message="Hello World!")