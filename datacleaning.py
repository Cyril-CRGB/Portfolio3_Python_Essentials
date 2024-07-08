import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Constant variables
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheet
SHEET = GSPREAD_CLIENT.open('OPTED-Dictionary')
the_dictionary = SHEET.worksheet('OPTED_Dictionary_sheet')

# Fetch all data
data = the_dictionary.get_all_values()

# Convert data to a list of dictionaries for easier access
dictionary_datacleaning = [
    {"Word": row[0], "Count": row[1], "POS": row[2], "Definition": row[3]}
    for row in data[1:] # Skipping the header row
]

# Function to get unique POS values
def get_unique_pos():
    pos_values = [entry['POS'] for entry in dictionary_datacleaning]
    unique_pos = list(set(pos_values))
    return unique_pos

# Function to count POS values
def get_pos_counts():
    pos_counts = {}
    for entry in dictionary_datacleaning:
        pos = entry['POS']
        if pos in pos_counts:
            pos_counts[pos] += 1
        else:
            pos_counts[pos] = 1
    return pos_counts

def main():
    unique_pos = get_unique_pos()
    print(f"\nUnique POS values: {unique_pos}")
    pos_count = get_pos_counts()
    print(f"\nUnique POS count: {pos_count}")
    pos_count_unique = get_pos_counts()
    print(f"\nUnique POS count unique: ")
    for pos, count in pos_count_unique.items():
        print(f"{pos}: {count}")


if __name__ == "__main__":
    main()