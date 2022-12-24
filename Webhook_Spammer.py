"""
Credits: Webhook spammer made byMusslord#1558
Discord: Musslord#1558
Github: Musslord1
DC_Server: https://discord.gg/Ynn9wNUQRf
"""
print("""

 _____ _           _        _ _ _     _   _____         _      _____                             
|   __|_|_____ ___| |___   | | | |___| |_|  |  |___ ___| |_   |   __|___ ___ _____ _____ ___ ___ 
|__   | |     | . | | -_|  | | | | -_| . |     | . | . | '_|  |__   | . | .'|     |     | -_|  _|
|_____|_|_|_|_|  _|_|___|  |_____|___|___|__|__|___|___|_,_|  |_____|  _|__,|_|_|_|_|_|_|___|_|  
              |_|                                                   |_|                          
                                    Made by Musslord#1558
                                    Github: Musslord1
                                    DC_Server: https://discord.gg/Ynn9wNUQRf
""")

import time
import requests
msg = input("Please Enter webhook Spam Message: ")
webhook = input("Please Enter webhook URL: ")
def spam(msg, webhook):
     for i in range(30):
         try:
             data = requests.post(webhook, json={'content': msg})
             if data.status_code == 204:
                 print(f"Sent MSG {msg}")
         except:
             print("Bad Webhook :" + webhook)
             time.sleep(5)
             exit()
counts = 1
while counts == 1:
    spam(msg, webhook)
