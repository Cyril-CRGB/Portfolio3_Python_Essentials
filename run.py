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
SHEET = GSPREAD_CLIENT.open('Portfolio3_distribution_keys')




def calculate_t_significant():
    """
    Calculate column F in the "Portfolio3_distribution_keys" sheet "Attendance"
    """
    # Use the sheet Attendance
    attendance = SHEET.worksheet('Attendance')
    # Get data from the sheet Attendance
    data = attendance.get_all_values()
    # Header row
    headers = data[0]
    # Initialize the updated data with headers
    updated_data = [headers]
    sum_t_significant = 0
    # Perform calculations and update the "T-Significant" column
    for row in data[1:]:
        if row[0] == 'Total': # row[0] = row headers
            continue # Skip iteration for 'Total' row
        travellers = convert_to_int(row[1])
        t_non_significant = convert_to_float(row[3])
        t_significant = round(travellers * (1- t_non_significant))
        sum_t_significant = sum_t_significant + t_significant
        row[5] = (str(t_significant))
        updated_data.append(row)
    # Update the "T-Significant" column in the Google Sheet
    attendance.update(updated_data)
    # Add sum_t_significant to column F, row 7
    sum_cell_range = "F7"
    attendance.update(sum_cell_range,[[str(sum_t_significant)]])

def calculate_PK_significant():
    """
    Calculate column G in the "Portfolio3_distribution_keys" sheet "Attendance"
    """
    # Use the sheet Attendance
    attendance = SHEET.worksheet('Attendance')
    # Get data from the sheet Attendance
    data = attendance.get_all_values()
    # Header row
    headers = data[0]
    # Initialize the updated data with headers
    updated_data = [headers]
    sum_pk_significant = 0
    # Perform calculations and update the "T-Significant" column
    for row in data[1:]:
        if row[0] == 'Total': # row[0] = row headers
            continue # Skip iteration for 'Total' row
        passenger_kilometres = convert_to_int(row[2])
        pk_non_significant = convert_to_float(row[4])
        pk_significant = round(passenger_kilometres * (1- pk_non_significant))
        sum_pk_significant = sum_pk_significant + pk_significant
        row[6] = (str(pk_significant))
        updated_data.append(row)
    # Update the "T-Significant" column in the Google Sheet
    attendance.update(updated_data)
    # Add sum_t_significant to column G, row 7
    sum_cell_range = "G7"
    attendance.update(sum_cell_range,[[str(sum_pk_significant)]])    


def convert_to_int(value):
    """
    Return a default value, 0, for empty or non-integer values
    """
    try:
        return int(value)
    except ValueError:
        return 0

def convert_to_float(value):
    """
    Return a default value, 0, for empty or non-float values
    """
    try:
        return float(value.replace(',', '.'))
    except ValueError:
        return 0.0


def main():
    """
    Run all program functions
    """
    calculate_t_significant()
    calculate_PK_significant()


main()
