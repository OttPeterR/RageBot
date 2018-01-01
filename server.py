import time
import sys
import requests
from flask import Flask, request
from RageBot import RageBot

app = Flask(__name__)

token_file = open("bot_token.txt", 'r')
bot_token = str(token_file.read())
token_file.close()
ragebot = RageBot()


def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token, method)


def process_message(update):
    data = {}

    data["chat_id"] = update["message"]["chat"]["id"]
    # to send back to the user, make it update["message"]["from"]["id"]

    response = ragebot.pass_message(update)
    if response is not None:
        data["text"] = response
        requests.post(get_url("sendMessage"), data=data)


@app.route("/{}".format(bot_token), methods=["POST"])
def process_update():
    if request.method == "POST":
        update = request.get_json()
        if "message" in update:
            process_message(update)
        return "ok!", 200


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
