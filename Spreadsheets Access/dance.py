# https://docs.gspread.org/en/latest/api.html#gspread.spreadsheet.Spreadsheet.share

from oauth2client.service_account import ServiceAccountCredentials as sac
import gspread, os

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

path = './Clouix/Spreadsheets'
jfile = 'ideationology-lab-b60654e44e37.json'
dir = os.path.join(path, jfile)

creds = sac.from_json_keyfile_name(dir, scope)
client = gspread.authorize(creds)

url = 'https://docs.google.com/spreadsheets/d/1Va2O06m-sBdjHmxkvl4TpkC-ghm6U8jkFxhShDHDWLE/edit?hl=en&forcehl=1#gid=117935182'
sheet = client.open_by_url(url)

sheet_instance = sheet.get_worksheet(0)
records_data = sheet_instance.get_all_records()

def fetch():
    Name=['Date (Y/M/D)']
    for i in records_data:
        Name.append(i['Name'])
    return Name[1:]

def mark(attend):
    import datetime
    dt = datetime.date.today()

    # attend = ['P', 'A', 'A']
    attend.insert(0, str(dt))

    worksheet_up = sheet.get_worksheet(1)
    sz = worksheet_up.col_values(1)

    if attend[0] != sz[-1]:
        sz = len(sz)+1
    else:
        sz = len(sz)

    worksheet_up.update(f'A{sz}', [attend])
    return attend
