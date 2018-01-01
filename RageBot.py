import RageBotUtility
from sentiment_analysis import analyzer


class RageBot:

    def __init__(self):
        self.user_rage_scores = {}
        self.analyzer = analyzer()
        self.rage_cool_down = 0.005

    def __get_chat(self, chatid):
        # getting chat dictionary, creating if not exists
        chat = None

        if chatid not in self.user_rage_scores:
            chat = {}
            self.user_rage_scores[chatid] = chat
        else:
            chat = self.user_rage_scores[chatid]
        return chat

    def __get_rage(self, username, chatid):
        username = str(username)
        chat = self.__get_chat(chatid)
        if username not in chat:
            chat[username] = 0
        return chat[username]

    def __update_user_rage(self, chatid, username, sentiment):
        username = str(username)

        chat = self.__get_chat(chatid)

        # adding sentiment to user, creating if not exists
        if username not in chat:
            chat[username] = sentiment
        else:
            chat[username] += sentiment

        return self.user_rage_scores[chatid][username]

    # update dictionary:
    # {u'message':
    #   {u'date': 1234567890, u'text': u'Message-Here',
    #   u'from':
    #     {u'username': u'User-Here', u'first_name': u'Name-Here',
    #     u'last_name': u'LastName-Here', u'is_bot': False,
    #     u'language_code': u'en', u'id': 1234567890},
    #     u'message_id': 1234567890,
    #     u'chat':
    #       {u'username': u'User-He re', u'first_name': u'Name-Here',
    #       u'last_name': u'LastName-Here', u'type': u'private',
    #       u'id': 1234567890}
    #   },
    #   u'update_id': 1234567890}

    def pass_message(self, update):

        print(str(update))

        if 'message' not in update or \
                'text' not in update['message']or \
                'id' not in update['message']['from']:
            print "problem with this message"
            return None

        # extract some data from the message
        message_text = update['message']['text']
        chatid = update['message']['chat']['id']
        username = update['message']['from']['id']

        # process commands
        if(message_text[0] == '/'):

            if(message_text[:10] == "/scorethis"):
                if message_text == "/scorethis" or \
                   message_text == "/scorethis@TheRageBot":
                    return "Usage: /scorethis I am bad at using commands"
                else:
                    score = self.analyzer.score_sentiment(message_text[10:])
                    return str(score.polarity)

            elif(message_text[:7] == "/myrage"):
                # lookup the chat and user and return their current rage rank
                return self.__get_rage(username, chatid)
            elif(message_text[:11] == "/getallrage"):
                return "You are: %s\n%s" \
                    % (str(username), str(self.user_rage_scores))
        # not a command, process messages
        else:
            score = self.analyzer.score_sentiment(message_text)
            self.__update_user_rage(chatid, username, score.polarity)
            return None

    def tick(self, seconds):
        for chat in self.user_rage_scores:
            for user in self.user_rage_scores[chat]:
                self.user_rage_scores[chat][user] =  \
                    RageBotUtility.cooldown(self.user_rage_scores[chat][user],
                                            self.rage_cool_down, seconds)
        return None
