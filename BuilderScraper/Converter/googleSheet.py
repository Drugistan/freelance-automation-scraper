import gspread
from gspread_dataframe import set_with_dataframe
import pandas as pd

gc = gspread.service_account(filename='credentials.json')
print(gc)

sheet = gc.open('Sheet Name')


worksheet = sheet.get_worksheet(0)

df = pd.read_csv('path/to/data.csv')

# Write the dataframe to the worksheet
set_with_dataframe(worksheet, df)


sheet_id = "1MnvXkijepa12pLNZMepmeRZfwBesz15zjnUT9VYcoh4"
