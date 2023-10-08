#MIT License
#Copyright (c) 2023, ©NovaNetworks

import sys
from logging import getLogger

LOGGER = getLogger(__name__)

# Required ENV
try:
    BOT_TOKEN = "6316910949:AAHdCdL8Uo2rxep0wsAUL4dWmtzDo7nRIIQ" # BOT TOKEN
    API_ID =  583311 # API ID
    API_HASH = "c67090d2c0a37d207385d04d9640045c" # API HASH
except Exception as e:
    LOGGER.error(f"Looks Like Something Is Missing!! Please Check Variables\n{e}")
    sys.exit(1)


TIMEZONE = "Asia/Kolkata" # YOUR TIME ZONE

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

SUDO = list({int(x)for x in ("6557686224").split()})

SUPPORT_CHAT = "uchihasasukebotsupport" # SUPPORT GROUP (ID OR USERNAME)

LOG_CHANNEL_ID = -1001825488060 #LOG GROUP ID FOR YOUR BOT

OWNER = list({int(x)for x in ("5829077962").split()}) #OWNER ID

DB_URL = "mongodb+srv://DarkLightning2008:Darkdeebu2008@cluster1.ut0l8mm.mongodb.net/?retryWrites=true&w=majority" # MONGO DB URL

SQL_URL = "postgres://mlckhdzh:***@tiny.db.elephantsql.com/mlckhdzh" # ELEPHANT SQL URL
