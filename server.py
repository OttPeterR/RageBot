import sys
import requests
from flask import Flask, request
from sentiment_analysis import analyzer

app = Flask(__name__)


if len(sys.argv) != 2:
    print("usage:\n\texport FLASK_APP=server.py\n\tflask run")
    exit()


token_file = open("bot_token.txt", 'r')
bot_token = str(token_file.read())
token_file.close()


def __init():
    global user_rage
    global analyzer
    user_rage = {}
    analyzer = analyzer()


__init()


def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token, method)


def process_message(update):
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
    #       u'last_name': u'LaseName-Here', u'type': u'private',
    #       u'id': 1234567890}
    #   },
    #   u'update_id': 1234567890}
    data = {}
    print update
    data["chat_id"] = update["message"]["from"]["id"]
    message_text = update['message']['text']
    score = analyzer.score_sentiment(message_text)
    if message_text == "yo":
        data["text"] = "yo yo man dawg"
        requests.post(get_url("sendMessage"), data=data)


@app.route("/{}".format(bot_token), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        if "message" in update:
            process_message(update)
        return "ok!", 200
