from shutil import copyfile
import os

copyfile('tosend.txt',
        'C://Users' + f'//{os.getlogin()}' + '//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//tosend.txt')
