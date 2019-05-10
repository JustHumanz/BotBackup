#!/usr/bin/python
import tarfile
import os
import time
import datetime
import glob
import telegram

db_host = "localhost" #database host
db_user = "!!!!1!" #database username
db_pass = "++***>>" #database password
db_name = ["????","???","????"] #backup multi databases
backup_dir = "/home/humanz/py/backup/db/" #folder backup
bot = telegram.Bot(token='!!111!1 USE YOUR BOT TOKEN !!111!1') #token telegram bot

dt = time.strftime('-%Y%m%d-%H%M%S')

def db_back():
    ab = len(db_name)
    ab = int(ab)
    for ab in range(ab):
        dump = "mysqldump -h " + db_host + " -u " + db_user + " -p" + db_pass + " " + db_name[ab] + " > "+ backup_dir + db_name[ab] + dt  + ".sql"
        os.system(dump)

    tar = tarfile.open("db"+dt+".tar.gz", "w:gz")
    for name in [backup_dir]:
        tar.add(name)
    tar.close()

    for rem in glob.iglob(os.path.join(backup_dir, '*.sql')):
        os.remove(rem) #remove sql file

    bot.send_document(chat_id=!!! use your chat id !!!, document=open("db"+dt+".tar.gz", 'rb')) #send file backup
    bot.send_message(chat_id=!!! use your chat id !!!, text="file backup databasenya Niichan")
    bot.send_sticker(chat_id=!!! use your chat id !!!,sticker="==== Use file id ====")
    bot.send_message(chat_id=!!! use your chat id !!!, text="tehehe kalau cuman segini gampang Niichan")
    os.remove("db"+dt+".tar.gz") #remove file backup

db_back() #if you use cron for schedule enable this

#schedule.every(1).days.do(db_back) #if you use schedule from python enable this
#while True:
#    schedule.run_pending()
