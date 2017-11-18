import telepot # for telegram use

def __handle_message(msg):
    print msg





if __name__ == '__main__':
    global bot

    startUp()
    bot = telepot.Bot(ConfigHelper.getBotID())
    bot.message_loop(__handle_message())
    print('%s is online...' % name)
    