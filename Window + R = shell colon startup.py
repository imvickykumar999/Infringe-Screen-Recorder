import shutil, os
filename = 'Window + R = shell colon startup.py'
shutil.move(filename, f'C://Users//{os.getlogin()}//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//{filename}')
