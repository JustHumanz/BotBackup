
import tarfile
import time
import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telebot


dt = time.strftime('%Y%m%d-%H%M%S')
bot = telegram.Bot(token='725295845:AAHsEoRjWgtFi0GACKX-r3JOSpZeKp_1hXU')

def back():
    tar = tarfile.open(".log"+dt+".tar.gz", "w:gz") #make compress file
    for name in ["/home/humanz/spectre-meltdown-checker.sh", "/home/humanz/arch.svg"]: #list file want to compress
        tar.add(name)
    tar.close()

    fz = os.path.getsize(".log"+dt+".tar.gz")
    if fz >= 1610612736: #max file size 1,5 GB
        os.remove(".log"+dt+".tar.gz")
        bot.send_chat_action(chat_id=386788173, action=telegram.ChatAction.TYPING)
        time.sleep(5)
        bot.send_sticker(chat_id=386788173,sticker="CAADBQADRAADTesNF66j3TlHno3lAg")
        bot.send_message(chat_id=386788173, text="file backupnya terlalu besar Niichan")
    else:
        bot.send_document(chat_id=386788173, document=open(".log"+dt+".tar.gz", 'rb'))
        bot.send_chat_action(chat_id=386788173, action=telegram.ChatAction.TYPING)
        time.sleep(2)
        bot.send_message(chat_id=386788173, text="file backupnya Niichan")
        bot.send_sticker(chat_id=386788173,sticker="CAADBQADTAADTesNF3-MpZLtvSNiAg")
        bot.send_chat_action(chat_id=386788173, action=telegram.ChatAction.TYPING)
        time.sleep(5)
        bot.send_message(chat_id=386788173, text="tehehe kalau cuman segini gampang Niichan")
        os.remove(".log"+dt+".tar.gz")

#back()

#if you use cron for schedule enable this

#schedule.every(1).days.do(back) #if you use schedule from python enable this
#while True:
#    schedule.run_pending()
