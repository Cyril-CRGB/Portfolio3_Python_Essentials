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

def calculate_pk_significant():
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


def calculate_structure_2():
    """
    Calculate and update table in the "Structure_2" worksheet
    """
    # Use the sheets "Attendance", "Structure_1" and "Structure_2"
    attendance = SHEET.worksheet('Attendance')
    structure_1 = SHEET.worksheet('Structure_1')
    structure_2 = SHEET.worksheet('Structure_2')

    # Get data from the "Attendance" worksheet
    attendance_data = attendance.get_all_values()
    attendance_headers = attendance_data[0] # First row of worksheet Attendance

    # Get data from the "Structure_1" worksheet
    structure_1_data = structure_1.get_all_values()
    structure_1_headers = structure_1_data[0] # First row of worksheet Structure_1
    
    # Initialize the updated data list for "Structure_2" with headers
    updated_data = [structure_1_headers]

    # Perform calculations and update the "Structure_2" worksheet
    for idx, row in enumerate(structure_1_data[1:], start=1):
        #print(idx)
        if row[0] == 'Total':
            continue # Skip iteration for 'Total' row
        company = row[0] # Get company names
        #print(company)
        updated_row = [company] # Each company name as a list
        sum_t_significant = 0
        sum_pk_significant = 0
        for col_idx, header in enumerate(structure_1_headers[1:], start=1):
            #print(col_idx, header)
            if header.endswith('_T'):
                t_percent = find_percentage(structure_1_data, company, header)
                #print(t_percent)
                t_significant = round(convert_to_int(attendance_data[idx][5]) * t_percent)
                #print(convert_to_int(attendance_data[idx][5]))
                sum_t_significant = sum_t_significant + t_significant
                #print(t_significant)
                updated_row.append(str(t_significant))
            else:
                pk_percent = find_percentage(structure_1_data, company, header)
                pk_significant = round(convert_to_int(attendance_data[idx][6]) * pk_percent)
                sum_pk_significant = sum_pk_significant + pk_significant
                updated_row.append(str(pk_significant))

        # Append the updated list 
        updated_data.append(updated_row)


    
    # Update the "Structure_2" worksheet in the Google Sheet
    structure_2.update(updated_data)
    result_travellers = verify_significant(sum_t_significant, convert_to_int(attendance_data[idx][5]))
    result_passenger = verify_significant(sum_pk_significant, convert_to_int(attendance_data[idx][6]))
    print(f"Data Travellers updated {result_travellers} in worksheet Structure_2")
    print(f"Data Passenger-kilometers updated {result_passenger} in worksheet Structure_2")


def update_sum_column_structure_2():
    """
    Calculate sum of each column in "Structure_2" worksheet
    """
    # Use the sheets "Structure_2"
    structure_2 = SHEET.worksheet('Structure_2')
    # Get data from the "Structure_2" worksheet
    structure_2_data = structure_2.get_all_values()
    # Initialize an empty list to store the sums for each column
    column_sums = [0] * len(structure_2_data[0]) 
    for column in range(1, 13):
        for row in range(1, 6):
            column_sums[column] += convert_to_int(structure_2_data[row][column])
    # Update row 7 with the column sums
    for column in range(1, 13): 
        structure_2.update(f"{chr(ord('A') + column)}7", [[str(column_sums[column])]])   



def verify_significant(data1, data2):
    """
    Print a warning to the console if sum_t_significant is != T_significant (in worksheet Attendance)
    """
    try:
        data1 == data2
        return "correctly"
    except:
        return "incorrectly"

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

def find_percentage(data, company, header):
    """
    Find the percentage value in the "Structure_1" worksheet corresponding to the company and header
    """
    try:
        col_idx = data[0].index(header)
        row_idx = [row[0] for row in data].index(company)
        return convert_to_float(data[row_idx][col_idx].strip('%')) / 100
    except ValueError:
        return 0.0


def main():
    """
    Run all program functions
    """
    #calculate_t_significant()
    #calculate_pk_significant()
    #calculate_structure_2()
    update_sum_column_structure_2()


main()
