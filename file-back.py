
import tarfile
import time
import os
import telegram
dt = time.strftime('%Y%m%d-%H%M%S')
bot = telegram.Bot(token='!!111!1 USE YOUR BOT TOKEN !!111!1')

def back():
    tar = tarfile.open(".log"+dt+".tar.gz", "w:gz") #make compress file
    for name in ["/home/humanz/ter.png", "/home/humanz/py/a.py"]: #list file want to compress
        tar.add(name)
    tar.close()

    fz = os.path.getsize(".log"+dt+".tar.gz")
    if fz >= 1610612736: #max file size 1,5 GB
        bot.send_sticker(chat_id=!!! use your chat id !!!,sticker="==== Use file id ====")
        bot.send_message(chat_id=!!! use your chat id !!!, text="file backupnya terlalu besar Niichan")
        os.remove(".log"+dt+".tar.gz")
    else:
        bot.send_document(chat_id=!!! use your chat id !!!, document=open(".log"+dt+".tar.gz", 'rb'))
        bot.send_message(chat_id=!!! use your chat id !!!, text="file backupnya Niichan")
        bot.send_sticker(chat_id=!!! use your chat id !!!,sticker="CAADBQADTAADTesNF3-MpZLtvSNiAg")
        bot.send_message(chat_id=!!! use your chat id !!!, text="tehehe kalau cuman segini gampang Niichan")
        os.remove(".log"+dt+".tar.gz")

back() #if you use cron for schedule enable this

#schedule.every(1).days.do(back) #if you use schedule from python enable this
#while True:
#    schedule.run_pending()
