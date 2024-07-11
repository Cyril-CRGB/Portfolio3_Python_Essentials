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

# Convert data to a list of dictionaries for easier access, excluding rows with empyt "POS" and duplicate words
seen_words = set()
dictionary_data = []
for row in data[1:]: # skipping the header row
    word, count, pos, definition = row[0], row[1], row[2], row[3]
    if pos and word not in seen_words:
        dictionary_data.append({"Word": word, "Count": count, "POS": pos, "Definition": definition})
        seen_words.add(word)

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

    print(f"\nDefinition: {definition}")
    print("\nChoose the correct word:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    while True: # Dealing with bad input
        guess = input("\nEnter the number of your choice: ")
        try:
            guess_index = int(guess) - 1
            if 0 <= guess_index < len(options):
                if options[guess_index].lower() == correct_word.lower():
                    print("\nCorrect!\n")
                else:
                    print(f"\nIncorrect. The correct word was '{correct_word}'.\n")
                break # Exit loop after a valid guess
            else:
                print("\nInvalid choice. Please enter a number corresponding to your choice.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

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

    print(f"\n\nWord: {word}")
    print("\nChoose the correct definition:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    while True: # Dealing with bad input
        guess = input("\nEnter the number of your choice: ")
        try:
            guess_index = int(guess) - 1
            if 0 <= guess_index < len(options):
                if options[guess_index].lower() == correct_definition.lower():
                    print("\nCorrect!\n")
                else:
                    print(f"\nIncorrect. The correct word was '{correct_definition}'.\n")
                break # Exit loop after a valid guess
            else:
                print("\nInvalid input. Please enter a number corresponding to your choice.\n")
        except ValueError:
            print("\nInvalid input. Please enter a number.\n")

# Main game loop
def main():
     print("\nWelcome to the Word Guessing Game! Wanna play?")
     while True:
        print("\nChoose a gameplay:")
        print("1. Guess the word from a definition")
        print("2. Guess the definition from a word")
        print("3. Exit")
        choice = input("\nEnter your choice (1, 2, or 3): ")

        if choice == '1':
            guess_word()
        elif choice == '2':
            guess_definition()
        elif choice == '3':
            print("\nThanks for playing!")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        
if __name__ == "__main__":
    main()