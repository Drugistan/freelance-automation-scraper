import csv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace with your Google Sheet ID
sheet_id = '1QlCSHL_4Sba976SOxOzzzJYj0y46OMgNfic7Tshqh9o'

# Replace with the path to your credentials JSON file
creds = service_account.Credentials.from_service_account_file('credentials.json')

# Create a new sheet named "Sheet1"
sheet_name = 'Builder'

# Read the CSV file
with open('builderOnline.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Build the Sheets API client
service = build('sheets', 'v4', credentials=creds)

# Add the data to the new sheet
body = {
    'values': rows
}
result = service.spreadsheets().values().update(
    spreadsheetId=sheet_id, range=sheet_name, valueInputOption='USER_ENTERED', body=body).execute()

print('{0} cells updated.'.format(result.get('updatedCells')))