
import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

def set_permission(
        jfile = 'client.json',
        url = 'https://docs.google.com/spreadsheets/d/103MOtyADixvjiKmg0XBNFo1FTy4fdxWJZ4ckyt4imMc/edit?usp=sharing',
        sheet_share = '18erecs080.vicky@rietjaipur.ac.in',
    ):

    creds = sac.from_json_keyfile_name(jfile, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(url) 
    sheet.share(sheet_share, perm_type='user', role='writer')

    sp = sheet.list_permissions()
    return sp 


sp = set_permission()
# print(sp)

for i in range(len(sp)):
    print(sp[i]['role'], sp[i]['emailAddress'])
