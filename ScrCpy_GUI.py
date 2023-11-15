
# https://github.com/imvickykumar999/ADB-Screen-Copy/releases
# pyinstaller --onefile ScrCpy_GUI.py

import os, json
import threading
from tkinter import *
from tkinterweb import HtmlFrame

ip = input('''
----------------------------------------
Press `CTRL + PAUSE/BREAK` keys to exit.

Press ENTER for default IP 
    192.168.0.103
----------------------------------------

Paste IP Address of Device : ''')


def task1():
    global ip
    print()

    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))

    if ip == '':
        ip = '192.168.0.103'

    while True:
        print()
        os.system(f'scrcpy --tcpip={ip}')


def task2():
    print()

    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))

    def power():
        os.system(f'adb -s {ip} shell input keyevent 26')

    def volup():
        os.system(f'adb -s {ip} shell input keyevent 24')

    def voldown():
        os.system(f'adb -s {ip} shell input keyevent 25')

    def submit(x):
        try: 
            if x == '': 
                os.system('Executable/keyevents.json')
            else:
                os.system(f'adb -s {ip} shell input keyevent {x}')
        except Exception as e: 
            print(e)

    def fun():
        key = num_list.get(num_list.curselection()[0])
        key = key.split(' : ')[0]
        os.system(f'adb -s {ip} shell input keyevent {key}')

    while True:
        root = Tk()
        root.geometry("300x600")
        root.title("ScrCpy GUI")
        root.config(bg="gray")

        try:
            bg = PhotoImage(file = "Executable/wallpaper.png") 
            label = Label(root, image = bg) 
            label.place(x = 0, y = 0) 
        except:
            frame = HtmlFrame(root)
            frame.load_website("https://github.com/imvickykumar999/ADB-Screen-Copy/blob/main/Projects/TkinterGUI/Executable/wallpaper.png?raw=true")
            frame.pack(fill="both", expand=True)

        try:
            rely3 = 0.7
            rely4 = 0.8
            rely5 = 0.9

            num_list = Listbox(root, height=15, width=30)
            with open('Executable/keyevents.json') as f:
                data = json.load(f)

            for i in data['key_events']:
                j = data['key_events'][i]
                k = j.split('adb shell input keyevent ')
                num_list.insert(k[1], f'{k[1]} : {i.split("key_")[1]}')

            num_list.place(relx=0.5, rely=0.4, anchor='center')
            get_num_btn = Button(root, bg='green', text="Run ADB", command=fun)
            get_num_btn.place(relx=0.5, rely=0.1, anchor='center')

        except:
            rely3 = 0.5
            rely4 = 0.6
            rely5 = 0.8

            event = StringVar()
            btn1 = Entry(root, textvariable = event)

            btn1.insert(0, '209') # Open Music App
            btn1.place(relx=0.5, rely=0.1, anchor='center')

            btn2 = Button(root, bg='green', text = 'Keyevent', command=lambda: submit(event.get()))
            btn2.place(relx=0.5, rely=0.2, anchor='center')

        btn3 = Button(root, text="Volume Up", command=volup)
        btn3.place(relx=0.5, rely=rely3, anchor='center')

        btn4 = Button(root, text="Volume Down", command=voldown)
        btn4.place(relx=0.5, rely=rely4, anchor='center')
        
        btn5 = Button(root, bg='red', text="Power ON / OFF", command=power)
        btn5.place(relx=0.5, rely=rely5, anchor='center')
        root.mainloop()


if __name__ == "__main__":
    os.system('color 2')
    print()

    print("ID of process running main program: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')  
  
    t1.start()
    t2.start()
  
    t1.join()
    t2.join()
