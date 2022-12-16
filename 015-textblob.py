>>> from textblob import TextBlob
>>> tweets = ("I was happy with the book", "this is awful", "Python is object oriented", "Python is awesome")
>>> for tw in tweets:
...     tw, TextBlob(tw).sentiment
...
('I was happy with the book', Sentiment(polarity=0.8, subjectivity=1.0))
('this is awful', Sentiment(polarity=-1.0, subjectivity=1.0))
('Python is object oriented', Sentiment(polarity=0.0, subjectivity=0.0))
('Python is awesome', Sentiment(polarity=1.0, subjectivity=1.0))