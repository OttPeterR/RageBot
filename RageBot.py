from sentiment_analysis import analyzer


class RageBot:

    def __init__(self):
        self.user_rage_scores = {}
        self.analyzer = analyzer()

    def pass_message(self, update):
        message_text = update['message']['text']
        if(message_text[0] == '/'):
            # the message is a command
            if(message_text[:10] == "/scorethis"):
                if len(message_text) == 10:
                    return "Usage: /scorethis I am bad at using commands"
                score = self.analyzer.score_sentiment(message_text[10:])
                return str(score.polarity)
            elif(message_text == "/myrage"):
                # lookup the chat and user and return their current rage rank
                return "--- under construction ---"
        else:
            score = self.analyzer.score_sentiment(message_text)
            # put it into the dictionary of users and their scores
            return None
