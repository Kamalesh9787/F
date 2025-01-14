import datetime
from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25599491")
    API_HASH = environ.get("API_HASH", "c8e3c0561cf148a6504f27b111fc3698")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "Forward-Bot") 
    DATABASE_URI = environ.get("DATABASE", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", 'itzz_introvert').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002037384930'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "-1002107651096") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
