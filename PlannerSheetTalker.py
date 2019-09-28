import gspread
from oauth2client.service_account import ServiceAccountCredentials




scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('PlannerSheets-800d5f115e3e.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('Planner').sheet1

rows=wks.get_all_records()
name = 'Parker'
for row in rows:
    if row['Student'] == name:
        print(row['Assignment'])
