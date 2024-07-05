import gspread
from google.oauth2.service_account import Credentials
# import numpy as np
# import pandas as pd

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Constant variables
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('OPTED-Dictionary')

the_dictionary = SHEET.worksheet('OPTED_Dictionary_sheet')

data = the_dictionary.get_all_values()

print(data)
