>>> import requests
# example from requests docs
>>> bad_r = requests.get('https://httpbin.org/status/404')
>>> bad_r.status_code
404
>>> bad_r.raise_for_status()
...
requests.exceptions.HTTPError: 404 Client Error

# good response
>>> good_r = requests.get('https://httpbin.org/status/200')
>>> good_r.raise_for_status()
>>>
# requests source > models.py
def raise_for_status(self):
    """Raises :class:`HTTPError`, if one occurred."""
    http_error_msg = ''
    ...
    if 400 <= self.status_code < 500:
        http_error_msg = u'%s Client Error: %s for url: %s' % (self.status_code, reason, self.url)

    elif 500 <= self.status_code < 600:
        http_error_msg = u'%s Server Error: %s for url: %s' % (self.status_code, reason, self.url)

    if http_error_msg:
        raise HTTPError(http_error_msg, response=self)