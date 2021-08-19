from shutil import copyfile
import os

copyfile('startup.py',
        'C://Users' + f'//{os.getlogin()}' + '//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//startup_copy.py')
