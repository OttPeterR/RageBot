import os
import ConfigParser
from Config import DefaultConfigCreator


class ConfigHelper():
    global loader
    global configParser
    global defaultConfigPath

    loaded = False
    configParser = ConfigParser.ConfigParser()

    # given the path to the config, load it
    def loadConfig(self):
        global configParser
        global loaded

        configParser.read(self.getConfigPath())
        loaded = True
        return

    def getConfigPath(self):
        return "./ragebot.cfg"


######################################
########### access methods ###########
######################################


# Telegram_Bot
telegram = 'Telegram_Bot'

def getBotID():
    return configParser.get(telegram, "bot_id")
