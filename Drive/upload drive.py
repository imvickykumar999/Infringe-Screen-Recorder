
def drive():
    # https://console.cloud.google.com/apis/credentials/consent?project=vicks-uploader
    # Tutorial : https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf

    from pydrive.drive import GoogleDrive
    from pydrive.auth import GoogleAuth

    # For using listdir()
    import os


    # Below code does the authentication
    # part of the code
    gauth = GoogleAuth()

    # Creates local webserver and auto
    # handles authentication.
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    # replace the value of this variable
    # with the absolute path of the directory

    path = "toupload"
    # path = r'C:\Users\Vicky\Desktop\Repository\Screen-Recorder'

    # iterating thought all the files/folder
    # of the desired directory
    for x in os.listdir(path):

        f = drive.CreateFile({'title': x})
        print(x)
        f.SetContentFile(os.path.join(path, x))
        f.Upload()

        # Due to a known bug in pydrive if we
        # don't empty the variable used to
        # upload the files to Google Drive the
        # file stays open in memory and causes a
        # memory leak, therefore preventing its
        # deletion
        f = None

drive()
