import gspread
from google.oauth2.service_account import Credentials
import numpy as np
import pandas as pd

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
# Constant variables2
CREDS2 = Credentials.from_service_account_file('creds2.json')
SCOPED_CREDS2 = CREDS2.with_scopes(SCOPE)
GSPREAD_CLIENT2 = gspread.authorize(SCOPED_CREDS2)
SHEET2 = GSPREAD_CLIENT2.open('Portfolio3_distribution_keys_2')



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

def calculate_percent_structure_3():
    """
    Calculate percentage and update "Structure_3" worksheet
    """
    # Use the sheets "Structure_2" and "Structure_3"
    structure_2 = SHEET.worksheet("Structure_2")
    structure_3 = SHEET2.worksheet("Structure_3")
    # Get data from the "Structure_2" worksheet
    structure_2_data = structure_2.get_all_values()

    # Calculate percentage and update "Structure_3" worksheet
    for row in range(1, 7):
        for col in range(1, 13):
            # Get the values from "Structure_2" and "Structure_3"
            value_structure_2_numerator = convert_to_float(structure_2_data[row][col].replace(',', ''))
            #print(value_structure_2_numerator)
            value_structure_2_denominator = convert_to_float(structure_2_data[6][col].replace(',', ''))
            #print(value_structure_2_denominator)
            # Calculate percentage
            percent = 100 * (value_structure_2_numerator / value_structure_2_denominator) if value_structure_2_denominator != 0 else 0
            # Round to four decimals
            percent_rounded = round(percent, 4)
            #print(percent_rounded)
            # Update "Structure_3" with the calculated percentage
            cell_ref = chr(ord('B') + col-1) + str(row+1)
            #print(cell_ref)
            structure_3.update(cell_ref, [[str(percent_rounded)]])


def calculate_average_km():
    """
    Calculate average kilometers and update "average_km" worksheet
    """
    # Use the sheets "Structure_2" and "Average_km"
    structure_2 = SHEET.worksheet("Structure_2")
    average_km = SHEET2.worksheet("Average_km")
    # Get data from the "Structure_2" worksheet
    structure_2_data = structure_2.get_all_values()
    # Calculate average kilometers and update "Average_km" worksheet
    for row in range(1,6):
        # Get the values from "Structure_2"
        adults_pk = convert_to_float(structure_2_data[row][2].replace(',', ''))
        adults_t = convert_to_float(structure_2_data[row][1].replace(',', ''))
        children_pk = convert_to_float(structure_2_data[row][4].replace(',', ''))
        children_t = convert_to_float(structure_2_data[row][3].replace(',', ''))
        subscription_adults_pk = convert_to_float(structure_2_data[row][6].replace(',', ''))
        subscription_adults_t = convert_to_float(structure_2_data[row][5].replace(',', ''))
        subscription_children_pk = convert_to_float(structure_2_data[row][8].replace(',', ''))
        subscription_children_t = convert_to_float(structure_2_data[row][7].replace(',', ''))
        tickets_other_pk = convert_to_float(structure_2_data[row][10].replace(',', ''))
        tickets_other_t = convert_to_float(structure_2_data[row][9].replace(',', ''))
        subscription_other_pk = convert_to_float(structure_2_data[row][12].replace(',', ''))
        subscription_other_t = convert_to_float(structure_2_data[row][11].replace(',', ''))
        # Calculate average kilometers row by row and column by column
        average_ticket_adults_km = adults_pk / adults_t if adults_t != 0 else 0
        average_ticket_children_km = children_pk / children_t if children_t != 0 else 0
        average_subscription_adults_km = subscription_adults_pk / subscription_adults_t if subscription_adults_t != 0 else 0
        average_subscription_children_km = subscription_children_pk / subscription_children_t if subscription_children_t != 0 else 0
        average_tickets_other_km = tickets_other_pk / tickets_other_t if tickets_other_t != 0 else 0
        average_subscription_other_km = subscription_other_pk / subscription_other_t if subscription_other_t != 0 else 0
        # Update "Average_km" with the calculated average kilometers
        average_km.update_cell((row + 1), 2, round(average_ticket_adults_km, 4))
        average_km.update_cell((row + 1), 3, round(average_ticket_children_km, 4))
        average_km.update_cell((row + 1), 4, round(average_subscription_adults_km, 4))
        average_km.update_cell((row + 1), 5, round(average_subscription_children_km, 4))
        average_km.update_cell((row + 1), 6, round(average_tickets_other_km, 4))
        average_km.update_cell((row + 1), 7, round(average_subscription_other_km, 4))

def calculate_regression():
    """
    Calculate regression and update "Regression" worksheet
    """
    # Use the sheets "Average_km" and "Regression" and "Fare_Grid"
    average_km = SHEET2.worksheet("Average_km")
    regression = SHEET2.worksheet("Regression")
    fare_grid = SHEET2.worksheet("Fare_Grid")
    # Get data from the "Average_km" worksheet
    average_km_data = average_km.get_all_values()
    headers = average_km_data[0]
    #print(headers)
    # Create a DataFrame from the data
    df = pd.DataFrame(average_km_data[1:], columns=headers)
    print(df)
    # Perform regression for each column
    for col in range(1, 7):
        # Check the header to determine the corresponding column in the worksheet Fare_Grid
        #print(col)
        header = headers[col]
        #print(header)
        if "Tickets_Adults" in header or "Tickets_Other" in header:
            grid_col = 1
            print("grid_col_1")
        elif "Tickets_Children" in header:
            grid_col = 2
            print("grid_col_2")
        elif "Subscriptions_Adults" in header or "Subscriptions_Other" in header:
            grid_col = 3
            print("grid_col_3")
        elif "Subscriptions_Children" in header:
            grid_col = 4
            print("grid_col_4")
        else:
            continue # Skip if the header doesn't match any category
        # Convert data to float and round up
        x = df[header].str.replace(',', '.').astype(float)
        print(x)
        # Get the data from the "Fare_Grid" worksheet
        grid_data = fare_grid.get_all_values()
        # Get the x and y values from the "Fare_Grid"
        x_grid = [float(row[0].replace(',', '.')) for row in grid_data[1:]]
        print(x_grid)
        y_grid = [float(row[grid_col].replace(',', '.')) for row in grid_data[1:]]
        print(y_grid)
        # Find the nearest value in x_grid for each x value in df
        indices = np.searchsorted(x_grid, x, side='left')
        # Get the corresponding y_grid value for each x value
        y_approx = np.array(y_grid)[indices]
        print(y_approx)
        # Calculate regression coefficients
        a, b = np.polyfit(x, y_approx, 1)
        print(a)
        print(b)
        # Update "Regression" with the calculated coefficients
        regression.update_cell(col+2, 2, round(b, 4))
        regression.update_cell(col+2, 3, round(a, 4))

def calculate_total_average_pk():
    """
    Calculate total average pk and update "Regression" worksheet
    """
    # Use the sheets "Structure_2" and "Regression"
    structure_2 = SHEET.worksheet("Structure_2")
    regression = SHEET2.worksheet("Regression")
    # Get data from the "Structure_2" worksheet
    structure_2_data = structure_2.get_all_values()
    # Get the values from "Structure_2"
    total_adults_pk = convert_to_float(structure_2_data[6][2].replace(',', ''))
    total_adults_t = convert_to_float(structure_2_data[6][1].replace(',', ''))
    total_children_pk = convert_to_float(structure_2_data[6][4].replace(',', ''))
    total_children_t = convert_to_float(structure_2_data[6][3].replace(',', ''))
    total_subscription_adults_pk = convert_to_float(structure_2_data[6][6].replace(',', ''))
    total_subscription_adults_t = convert_to_float(structure_2_data[6][5].replace(',', ''))
    total_subscription_children_pk = convert_to_float(structure_2_data[6][8].replace(',', ''))
    total_subscription_children_t = convert_to_float(structure_2_data[6][7].replace(',', ''))
    total_tickets_other_pk = convert_to_float(structure_2_data[6][10].replace(',', ''))
    total_tickets_other_t = convert_to_float(structure_2_data[6][9].replace(',', ''))
    total_subscription_other_pk = convert_to_float(structure_2_data[6][12].replace(',', ''))
    total_subscription_other_t = convert_to_float(structure_2_data[6][11].replace(',', ''))
    # Calculate total average kilometers row by row and column by column
    total_average_ticket_adults_km = total_adults_pk / total_adults_t if total_adults_t != 0 else 0
    total_average_ticket_children_km = total_children_pk / total_children_t if total_children_t != 0 else 0
    total_average_subscription_adults_km = total_subscription_adults_pk / total_subscription_adults_t if total_subscription_adults_t != 0 else 0
    total_average_subscription_children_km = total_subscription_children_pk / total_subscription_children_t if total_subscription_children_t != 0 else 0
    total_average_tickets_other_km = total_tickets_other_pk / total_tickets_other_t if total_tickets_other_t != 0 else 0
    total_average_subscription_other_km = total_subscription_other_pk / total_subscription_other_t if total_subscription_other_t != 0 else 0
    # Update "Average_km" with the calculated average kilometers
    regression.update_cell((3), 4, round(total_average_ticket_adults_km, 4))
    regression.update_cell((4), 4, round(total_average_ticket_children_km, 4))
    regression.update_cell((5), 4, round(total_average_subscription_adults_km, 4))
    regression.update_cell((6), 4, round(total_average_subscription_children_km, 4))
    regression.update_cell((7), 4, round(total_average_tickets_other_km, 4))
    regression.update_cell((8), 4, round(total_average_subscription_other_km, 4))

def calculate_totalprice():
    """
    Calculate total price and update "Regression" worksheet
    """
    # Use the sheets "Regression"
    regression = SHEET2.worksheet("Regression")
    # Get data from the "Structure_2" worksheet
    regression_data = regression.get_all_values()
    # find data and operate with them
    for i in range(2, 8):
        totalprices = convert_to_float(regression_data[i][1].replace(',', '.')) + (convert_to_float(regression_data[i][2].replace(',', '.')) * convert_to_float(regression_data[i][3].replace(',', '.')))
        # Update regression worksheet with totalprices
        regression.update_cell((i + 1), 5, round(totalprices, 4))

def calculate_sharetravellers():
    """
    Calculate share travellers and update "Regression" worksheet
    """
    # Use the sheets "Regression"
    regression = SHEET2.worksheet("Regression")
    # Get data from the "Structure_2" worksheet
    regression_data = regression.get_all_values()
    # find data and operate with them
    for i in range(2, 8):
        sharetravellers = convert_to_float(regression_data[i][1].replace(',', '.')) / convert_to_float(regression_data[i][4].replace(',', '.'))
        # Update regression worksheet with totalprices
        regression.update_cell((i + 1), 6, round(sharetravellers, 2))

def calculate_sharePassengerkilometers():
    """
    Calculate Share Passenger Kilometers and update "Regression" worksheet
    """
    # Use the sheets "Regression"
    regression = SHEET2.worksheet("Regression")
    # Get data from the "Structure_2" worksheet
    regression_data = regression.get_all_values()
    # find data and operate with them
    for i in range(2, 8):
        sharepassengerkilometers = convert_to_float(regression_data[i][2].replace(',', '.')) * convert_to_float(regression_data[i][3].replace(',', '.')) / convert_to_float(regression_data[i][4].replace(',', '.'))
        # Update regression worksheet with totalprices
        regression.update_cell((i + 1), 7, round(sharepassengerkilometers, 2))

def calculate_keys():
    """
    Calculate keys for each company and update "Keys" worksheet
    """
    # Use the sheets "Structure_3, "Turnover" and "Regression"
    structure_3 = SHEET2.worksheet("Structure_3")
    turnover = SHEET2.worksheet("Turnover")
    regression = SHEET2.worksheet("Regression")
    # Get data from the worksheets
    structure_3_data = structure_3.get_all_values()
    turnover_data = turnover.get_all_values()
    regression_data = regression.get_all_values()
    # find data and operate with them
    listnew = []
    listnew2 = []
    listnew3 = []
    for l in range(2, 8):
        ufokey_sharetravellers = convert_to_float(regression_data[l][5].replace(',', '.'))
        listnew.append(ufokey_sharetravellers)
    
    for i in range(1, 13):
        if i % 2 !=0:
            ufokey_structure_3 = convert_to_float(structure_3_data[1][i].replace(',', '.'))
            listnew2.append(ufokey_structure_3)
        else:
            continue
    for x, y in zip(listnew, listnew2):
        multipl = x * y
        listnew3.append(multipl)
    print(listnew3)
        #print(ufokey_structure_3)
        #print(ufokey_turnover)
        #print(ufokey_regression)
        # Update regression worksheet with totalprices
        #regression.update_cell((i + 1), 7, round(sharepassengerkilometers, 2))

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
    #update_sum_column_structure_2()
    #calculate_percent_structure_3()
    #calculate_average_km()
    #calculate_regression()
    #calculate_total_average_pk()
    #calculate_totalprice()
    #calculate_sharetravellers()
    #calculate_sharePassengerkilometers()
    calculate_keys()

main()
