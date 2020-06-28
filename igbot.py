import os
import time
while True:
    os.system('python follower.py')
    os.system('python chatbot.py')
    os.system('python commentor.py')
    time.sleep(60*60*1)#1 hour
    
