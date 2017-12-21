import sys
from pprint import pprint
import requests

if len(sys.argv) != 3:
    print("usage:\n\tpython server.py <your-bot-id> <your-https-url>")
    exit()

bot_token = sys.argv[1]
https_url = sys.argv[2]

test_url = https_url+"/{}".format(bot_token)

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

r = requests.get(get_url("setWebhook"), data={"url": test_url})
r = requests.get(get_url("getWebhookInfo"))
pprint(r.status_code)
pprint(r.json())
