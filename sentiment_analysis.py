from textblob import TextBlob


class analyzer():

    def __init__(self):
        self.analyzer = None

    def score_sentiment(self, text):
        self.analyzer = TextBlob(text)
        return self.analyzer.sentiment
