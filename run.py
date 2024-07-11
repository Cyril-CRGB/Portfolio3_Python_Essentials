import gspread
from google.oauth2.service_account import Credentials
import random
import os
import platform


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

# Convert data to a list of dictionaries for easier access, excluding rows with empty "POS" and duplicate words
seen_words = set()
dictionary_data = []
for row in data[1:]: # skipping the header row
    word, count, pos, definition = row[0], row[1], row[2], row[3]
    if pos and word not in seen_words:
        dictionary_data.append({"Word": word, "Count": count, "POS": pos, "Definition": definition})
        seen_words.add(word)

# Function to clear_console
def clear_console():
    os_system = platform.system()
    if os_system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#get_random_options
#get_random_options_definition

# Unified function to get random options for multiple choice
def get_random_options(correct_value, field):
    values = [entry[field] for entry in dictionary_data if entry[field] != correct_value]
    return random.sample(values, 2)

# Function to guess the word from a given definition with multiple choice options
def guess_word():
    clear_console() # Making space and the game more enjoyable
    while True: # Allowing the player to keep playing until is done
        entry = random.choice(dictionary_data)
        correct_word = entry['Word']
        definition = entry['Definition']

        # Get random options exlcuding the correct word
        options = get_random_options(correct_word, 'Word')
        options.append(correct_word)
        random.shuffle(options)

        print("\nDefinition:")
        print(f"\n-->     {definition}")
        print("\nChoose the right word:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        # Adding two options to make the game funnier
        print("----or-----------")
        print(f"{len(options)+1}. Change gameplay")
        print(f"{len(options)+2}. Quit")

        while True: # Dealing with bad input
            guess = input("\nEnter the number of your choice: ")
            try:
                guess_index = int(guess) - 1
                if 0 <= guess_index < len(options):
                    if options[guess_index].lower() == correct_word.lower():
                        clear_console() # Making space and the game more enjoyable
                        print("\nCorrect!\n")
                    else:
                        clear_console() # Making space and the game more enjoyable
                        print(f"\nIncorrect. The correct word was '{correct_word}'.\n")
                    break # Exit loop after a valid guess
                elif guess_index == len(options):
                    return "change"
                elif guess_index == len(options) + 1:
                    return "quit"
                else:
                    clear_console() # Making space and the game more enjoyable
                    print("\nInvalid choice. Please enter a number corresponding to your choice.\n")
            except ValueError:
                clear_console() # Making space and the game more enjoyable
                print("\nInvalid input. Please enter a number.\n")


# Function to guess the definition from a given word with multiple choice options
def guess_definition():
    clear_console() # Making space and the game more enjoyable
    while True: # Allowing the player to keep playing until is done
        entry = random.choice(dictionary_data)
        word = entry['Word']
        correct_definition = entry['Definition']

        # Get random options exlcuding the correct definition
        options = get_random_options(correct_definition, 'Definition')
        options.append(correct_definition)
        random.shuffle(options)

        print("\nWord:")
        print(f"\n-->     {word}")
        print("\nChoose the right definition:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        # Adding two options to make the game funnier
        print("----or-----------")
        print(f"{len(options)+1}. Change gameplay")
        print(f"{len(options)+2}. Quit")

        while True: # Dealing with bad input
            guess = input("\nEnter the number of your choice: ")
            try:
                guess_index = int(guess) - 1
                if 0 <= guess_index < len(options):
                    if options[guess_index].lower() == correct_definition.lower():
                        clear_console() # Making space and the game more enjoyable
                        print("\nCorrect!\n")
                    else:
                        clear_console() # Making space and the game more enjoyable
                        print(f"\nIncorrect. The correct word was '{correct_definition}'.\n")
                    break # Exit loop after a valid guess
                elif guess_index == len(options):
                    return "change"
                elif guess_index == len(options) + 1:
                    return "quit"
                else:
                    clear_console() # Making space and the game more enjoyable
                    print("\nInvalid input. Please enter a number corresponding to your choice.\n")
            except ValueError:
                clear_console() # Making space and the game more enjoyable
                print("\nInvalid input. Please enter a number.\n")


# Main game loop
def main():
    clear_console() # Making space and the game more enjoyable
    print("\nWelcome to the Word Guessing Game! Wanna play?")
    while True:
        choice = input("\nYes(y) or No(n): ")
        if choice.lower() == 'y':
            clear_console() # Making space and the game more enjoyable
            while True:
                print("\nNice! Choose a gameplay:")
                print("1. Guess the word from a definition")
                print("2. Guess the definition from a word")
                print("3. Exit")
                gameplay_choice = input("\nEnter your choice (1, 2, or 3): ")
                if gameplay_choice == '1':
                    while True:
                        result = guess_word()
                        if result == "change":
                            break
                        elif result == "quit":
                            clear_console() # Making space and the game more enjoyable
                            print("\nThanks for playing!\n")
                            return
                elif gameplay_choice == '2':
                    while True:
                        result = guess_definition()
                        if result == "change":
                            break
                        elif result == "quit":
                            clear_console() # Making space and the game more enjoyable
                            print("\nThanks for playing!\n")
                            print("\nTo play again, click on 'run programm'\n")
                            return
                elif gameplay_choice == '3':
                    clear_console() # Making space and the game more enjoyable
                    print("\nThanks for playing!\n")
                    print("\nTo play again, click on 'run programm'\n")
                    return
                else:
                    clear_console() # Making space and the game more enjoyable
                    print("\nInvalid choice. Please try again.\n")
        elif choice.lower() == 'n':
            clear_console() # Making space and the game more enjoyable
            print("\nToo sad :( we hope to see you soon!\n")
            print("\nTo play again, click on 'run programm'\n")
            return        
        else:
            clear_console() # Making space and the game more enjoyable
            print("\nInvalid choice. Please try again.")

        
        
if __name__ == "__main__":
    main()