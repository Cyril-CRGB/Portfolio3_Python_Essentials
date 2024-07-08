import gspread
from google.oauth2.service_account import Credentials
import random


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
dictionary_data = [
    {"Word": row[0], "Count": row[1], "POS": row[2], "Definition": row[3]}
    for row in data[1:] # Skipping the header row
]

# Function to get random options for multiple choice
def get_random_options(correct_word):
    words = [entry['Word'] for entry in dictionary_data if entry['Word'] != correct_word]
    return random.sample(words, 2)

# Function to guess the word from a given definition with multiple choice options
def guess_word():
    entry = random.choice(dictionary_data)
    correct_word = entry['Word']
    definition = entry['Definition']

    # Get random options exlcuding the correct word
    options = get_random_options(correct_word)
    options.append(correct_word)
    random.shuffle(options)

    print(f"Definition: {definition}")
    print("Choose the correct word:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    guess = input("Enter the number of your choice: ")

    try:
        guess_index = int(guess) - 1
        if options[guess_index].lower() == correct_word.lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct word was '{correct_word}'.")
    except(ValueError, IndexError):
        print("Invalid input. Please enter a number corresponding to your choice.")

# Function to get random options for multiple choice
def get_random_options_definition(correct_definition):
    definitions = [entry['Definition'] for entry in dictionary_data if entry['Definition'] != correct_definition]
    return random.sample(definitions, 2)


# Function to guess the definition from a given word with multiple choice options
def guess_definition():
    entry = random.choice(dictionary_data)
    word = entry['Word']
    correct_definition = entry['Definition']

    # Get random options exlcuding the correct definition
    options = get_random_options(correct_definition)
    options.append(correct_definition)
    random.shuffle(options)

    print(f"Word: {word}")
    print("Choose the correct definition:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    guess = input("Enter the number of your choice: ")
    
    try:
        guess_index = int(guess) - 1
        if options[guess_index].lower() == correct_definition.lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct word was '{correct_definition}'.")
    except(ValueError, IndexError):
        print("Invalid input. Please enter a number corresponding to your choice.")

# Main game loop
def main():
    # print("Welcome to the Word Guessing Game!")
    # while True:
    #    print("\nChoose an option:")
    #    print("1. Guess the word from a definition")
    #    print("2. Guess the definition from a word")
    #    print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            guess_word()
        elif choice == '2':
            guess_definition()
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        
if __name__ == "__main__":
    main()