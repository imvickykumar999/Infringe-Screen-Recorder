
# Helpful links in this code...
# -----------------------------------
# https://stackoverflow.com/a/70825050/11493297
# https://docs.google.com/spreadsheets/d/18eQ5K7B-A1XLxmcy-W_ZlZ9ddDMnxhaIqzyHn0XDDOM/edit?resourcekey#gid=30127793
# https://console.cloud.google.com/apis/api/drive.googleapis.com/credentials?project=ideationology-lab
# https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/
# https://www.youtube.com/watch?v=7dGPLKD-FeM
# https://www.geeksforgeeks.org/collecting-data-with-google-forms-and-pandas/


def public_data():
    try:
        # >>> WARNING : for publicly open sheets
        import pandas as pd

        sheet_id = '1E-SpPEszLcyEysQNHAB12LfCIhj_v0HRbRHs21msd7Y'
        url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'

        df = pd.read_csv(url)
        file_name = 'Contact Information (Responses).csv'
        df.to_csv(file_name)

        import os
        os.startfile(file_name)

    except Exception as e:
        print(e)


def private_data():

    # pip3 install gspread
    # pip3 install --upgrade google-api-python-client
    # pip3 install oauth2client

    from oauth2client.service_account import ServiceAccountCredentials as sac

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    jfile = 'ideationology-lab-b60654e44e37.json'
    creds = sac.from_json_keyfile_name(jfile, scope)

    import gspread
    client = gspread.authorize(creds)

    url = 'https://docs.google.com/spreadsheets/d/18eQ5K7B-A1XLxmcy-W_ZlZ9ddDMnxhaIqzyHn0XDDOM/edit?usp=sharing'
    sheet = client.open_by_url(url)

    per = sheet.list_permissions()
    for i in per:
        print(i['emailAddress'])

    def worksheet_count():
        flag = True
        i = 0

        while flag:
            try:
                ith = sheet.get_worksheet(i)
                i += 1
                # print(ith)
            except Exception as e:
                # print(e)
                flag = False

        print(f'Total worksheet = {i}')

    worksheet_count()

    sheet_instance = sheet.get_worksheet(0)
    records_data = sheet_instance.get_all_records()

    import pandas as pd
    records_df = pd.DataFrame.from_dict(records_data)

    name = 'Internship Details (Responses).csv'
    records_df.to_csv(name)

    import os
    os.startfile(name)
