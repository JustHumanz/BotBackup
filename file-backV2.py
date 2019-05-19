import telebot
import os
import tarfile
import time
import glob
import re

bot = telebot.TeleBot("725295845:AAHsEoRjWgtFi0GACKX-r3JOSpZeKp_1hXU")
dt = time.strftime('%Y%m%d-%H%M%S')
chatid = "386788173"

#File Backup
foln = ["/home/humanz/ss.sh","/home/humanz/arch.svg"]


db_host = "localhost" #database host
db_user = "root" #database username
db_pass = "321" #database password
db_name = ["coba","test","kkk"] #backup multi databases
backup_dir = "/home/humanz/py/backup/db/" #folder backup


def ba():
    tar = tarfile.open("log.tar.gz", "w:gz") #make compress file
    for name in [*foln]: #list file want to compress
        tar.add(name)
    tar.close()
    fz = os.path.getsize("log.tar.gz")
    if fz >= 1610612736:
        bot.send_message(chatid, "File Backup Terlalu besar Niichan")
        bot.send_sticker(chatid, "CAADBQADRAADTesNF66j3TlHno3lAg")
        return
    else:
        bot.send_sticker(chatid, "CAADBQADTAADTesNF3-MpZLtvSNiAg")
        bot.send_message(chatid, "Done,delivering now")

def sl():

    ab = len(db_name)
    ab = int(ab)
    for ab in range(ab):
        dump = "mysqldump -h " + db_host + " -u " + db_user + " -p" + db_pass + " " + db_name[ab] + " > "+ backup_dir + db_name[ab] + dt  + ".sql"
        os.system(dump)

    tar = tarfile.open("db.tar.gz", "w:gz")
    for name in [backup_dir]:
        tar.add(name)
    tar.close()

    for rem in glob.iglob(os.path.join(backup_dir, '*.sql')):
        os.remove(rem) #remove sql file


@bot.message_handler(commands=['start'])
def handle_message(message):
    bot.send_sticker(chatid, "CAADBQADPgADTesNF4ySjKlXZpusAg")
    bot.reply_to(message, "Welcome Back Niichan\n use /start to start bot\n use /help to show help menu\n use /info to show about this bot")

@bot.message_handler(commands=['info'])
def handle_message(message):
    bot.send_sticker(chatid, "CAADBQADPAADTesNF5Z43xR8XcmBAg")
    bot.reply_to(message, "Kano2525 Bot,Create by Just_Humanz\nIG : instagram.com/aldin0x1101\nFB : fb.me/kaitothethief\nGithub : github.com/JustHumanz")

@bot.message_handler(commands=['help'])
def handle_message(message):
    bot.send_sticker(chatid, "CAADBQAD4wADkpVwBBTO3RBrbMw4Ag")
    bot.reply_to(message, "Read The FUCKING README.md")


@bot.message_handler(regexp="Backup file")
def handle_message(message):
    bot.reply_to(message, "Yokai Niichan")
    time.sleep(0.5)
    bot.send_sticker(chatid, "CAADBQADOAADTesNF1E8S1h3wglEAg")
    time.sleep(0.5)
    bot.send_message(chatid, "Processing compress file")
    ba()
    time.sleep(2)
    os.rename("log.tar.gz","file"+dt+".tar.gz")
    docc = open("file"+dt+".tar.gz", 'rb')
    bot.send_chat_action(chatid, "upload_document")
    time.sleep(2)
    bot.send_document(chatid, docc)
    os.remove("file"+dt+".tar.gz")

@bot.message_handler(regexp="Backup sql")
def handle_message(message):
    bot.reply_to(message, "Yokai Niichan")
    time.sleep(0.5)
    bot.send_sticker(chatid, "CAADBQADOAADTesNF1E8S1h3wglEAg")
    time.sleep(0.5)
    bot.send_message(chatid, "Backup database and compress file")
    sl()
    time.sleep(2)
    os.rename("db.tar.gz","file_db"+dt+".tar.gz")
    docc_db = open("file_db"+dt+".tar.gz", 'rb')
    bot.send_chat_action(chatid, "upload_document")
    time.sleep(2)
    bot.send_document(chatid, docc_db)
    os.remove("file_db"+dt+".tar.gz")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if re.search("^(?!Backup file|Backup sql\\.).*", message.text):
        bot.reply_to(message, "Worng Input Niichan")
        bot.send_sticker(chatid, "CAADBQADTgADTesNFytyrfCZbu8VAg")


bot.polling()
