
import os
import threading

ip = input('''
Press `CTRL + PAUSE/BREAK` keys to exit.

    Volume Up   : >>> 24
    Volume Down : >>> 25
    Power       : >>> 26

(Press ENTER for default IP 192.168.0.103)
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

    while True:
        x = input('>>> ')
        if x == '':
            x = 26
        os.system(f'adb shell input keyevent {x}')


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
