<p align="center">
  <b> Bot Backup </b>
  </p>
<p align="center"> Kano2525_Bot </p>    

![screenshot](https://raw.githubusercontent.com/JustHumanz/BotBackup/master/img/SS.png)  

# Description  
This bot telegram bot made my python,this bot can make backup file or database and send it via telegram  
This bot will help you if you need backup your data in server but you not have time to manualy backup  

# How to install
```
git clone https://github.com/JustHumanz/BotBackup  
cd BotBackup  
sudo pip install -r requeriments.txt  
```

# How to Use
<b>change with your bot ID</b>  
```
bot = telebot.TeleBot("!!! YOUR BOT ID!!!")  
```
<b>change with your chatid</b>    
```
chatid = "!! Your chat_id !!"  
```  
<b>change with file you want to backup</b>   
```
foln = ["!!! file or a directory !!!","*** file or a directory ***"]
```
Example
```
foln = ["/home/humanz/ss.sh","/home/humanz/arch.svg"]
```
<b>change with your database config </b>
```
db_host = "!! Database hosts !!"
db_user = "!! Database username !!"
db_pass = "!! Database password !!"
db_name = ["!! Database you want to backup !!","!! Database you want to backup !!","!! Database you want to backup !!"]
backup_dir = "!! directory backup of .sql !!"
```
Example
```
db_host = "localhost"
db_user = "root"
db_pass = "321"
db_name = ["coba","test","kkk"]
backup_dir = "/home/humanz/py/backup/db/"
```
and the last is run the script
```
python file-backV2.py
```
# Video
![video](https://raw.githubusercontent.com/JustHumanz/BotBackup/master/img/demo.mkv)  
