# Portfolio 3 - Python Essential

## Word guess game

## Project description

This website is a word game based on a free english dictionary. 

The goals for the end user are:
- to test his/her knowledges of the english language
- to learn new words
- to play
- to have fun

The player can chose between two ways of playing. Either try to guess the definition of a given word, or the opposite, try to guess a word of a given definition.

The word and the definition that the player is looking for are randomly chosen and given by the programm.

The player can chose amongs 3 solutions, only one of them is true, the 2 others are randomly chosen by the programm. All given choices suggested by the programm must be different from one another. No repeatition is allowed.

Have fun with the game, and learn new words!


## Features:

This app contains 7 functions, including the main fonction.

The global function calls the 12 major and the 12 major call the 4 minor for calulation purpose.

1) clear_console(): allows to clear the command prompt in order to keep the command line as clean as possible, it makes easier to read the prompt 
2) get_random_options(correct_value, field): allows to generate random values for the functions "guess_word" and "guess_definition"
3) guess_word(): allows to get a question about a random word
4) guess_definition(): allows to get a question about a random definition
5) first_question(): the "yes or no" question at the begining
6) second_question(): the second question "choose a gameplay"
7) main(): allows the player to enjoy himself/herself


## Testing:
### buggs : 
I noticed that the data used had flaws in it. For instance 
- There is nine time the letter A, and with that all the letters of the alphabet. Which I found redoundant. Therefore I decided to deal with them.
    -> SOLUTION:
            1) erase all rows that contains "1" inside the column "Count" -> done
- There were POS (word positions) that had simply no position, it only contained empty braquets "", it is the case for alphabet letters but also for proper noun.
    -> SOLUTION: 
            1) erase the "" from database, not working I reached APIError [429]: Quota exceeded for quota metric
            2) include exception for the programm to exclude empty POS to be selected for the game
- That some entry in the data were missing or contained - #NAME? - witch I decided to remove.
    -> SOLUTION:
            1) remove the rows that contains an error -> done
- That some 2 words had in column "Count" 70 and 83, here there are: 
            a) ", a , or an . PCP. It is presumably an older spelling of scanned. --2."
            b) ", a , or an . PCP. It is presumably an older spelling of scanned. --2. Specifically"
    -> SOLUTION:
            1) remove those two words, because they do not had value to the game -> done
- That some POS (word positions) where unique, or reversed and could be joined to another without loosing much meaning: "n. & v.", "v. & n." and "n. & v. t."
    -> SOLUTION:
            1) leave it as it is, I will not use POS
- That some word where repeated for each definition they can have. 
    -> SOLUTION: 
            1) I decided to leave them out too. Delete every 2nd and more repeatition of the same word
- I verified that there is no empty rows

Thus I decided to analyse the data further to insure the data was meaningfull for the purpose of the game. I created a new python file called "datacleaning.py", and I duplicated the sheet of my googlesheet, renamed it "Original.." in order to keep trac of the modification of the data.

### Dealing with exception:
By the functions "guess_word" and "guess_definition", if an Invalid input is given, it takes the player out of the function, back to the "main" function, although the player might still want to keep trying.


#### Testing response from the programm:

1) first question "yes/no":

        a) Invalid input = "z"
           Output = coming back! with error message

                <img src="Readmepics/Printscreen_2.jpg" alt="ReadmePicture2">

        b) Valid input = "n"
           Output = quit!

                <img src="Readmepics/Printscreen_4.jpg" alt="ReadmePicture4">

        c) Valid input = "y"
           Output = game!

                <img src="Readmepics/Printscreen_6.jpg" alt="ReadmePicture6">


2) second question "choose a gameplay":

        a) Invalid input = "8"
           Output = coming back! with error message

                <img src="Readmepics/Printscreen_8.jpg" alt="ReadmePicture8">

        b) Valid input = "1"
           Output = game question "Guess a word"

                <img src="Readmepics/Printscreen_10.jpg" alt="ReadmePicture10">

        c) Valid input = "2"
           Output = game question "Guess a definition"

                <img src="Readmepics/Printscreen_12.jpg" alt="ReadmePicture12">

        d) Valid input = "3"
           Output = exit game

                <img src="Readmepics/Printscreen_14.jpg" alt="ReadmePicture14">


3) game question "Guess a word":

        a) Invalid input = "/////"
           Output = giving the possible choices again with error message

                <img src="Readmepics/Printscreen_16.jpg" alt="ReadmePicture16">

        b) Valid input = "1" to "3"
                A) right answer:
                   Output = "Congrats! Your answer is Correct!" + next question

                        <img src="Readmepics/Printscreen_17.jpg" alt="ReadmePicture17">

                B) wrong answer:
                   Output = "Incorrect. The correct word was ..." + next question

                        <img src="Readmepics/Printscreen_18.jpg" alt="ReadmePicture18">

        c) Valid input = "4"
           Output = back to "Choose a gameplay" see point 2 above

                <img src="Readmepics/Printscreen_19.jpg" alt="ReadmePicture19">

        d) Valid input = "5"
           Output = exit game

                <img src="Readmepics/Printscreen_20.jpg" alt="ReadmePicture20">


4) game question "Guess a definition":

        a) Invalid input = "&%/()"
           Output = giving the possible choices again with error message

                <img src="Readmepics/Printscreen_21.jpg" alt="ReadmePicture21">

        b) Valid input "1" to "3"

                A) right answer:

                        <img src="Readmepics/Printscreen_22.jpg" alt="ReadmePicture22"> 

                B) wrong answer:

                        <img src="Readmepics/Printscreen_23.jpg" alt="ReadmePicture23"> 

        c) Valid input = "4"
           Output = back to "Choose a gameplay" see point 2 above

                <img src="Readmepics/Printscreen_24.jpg" alt="ReadmePicture24"> 

        d) Valid input = "5"
           Output = exit game

                <img src="Readmepics/Printscreen_25.jpg" alt="ReadmePicture25"> 
                        




## Technologies Used

- Python

## Special library

- none

## Credits
https://www.kaggle.com/datasets/dfydata/the-online-plain-text-english-dictionary-opted?resource=download
The Online Plain Text English Dictionary (OPTED)
Dictionary in CSV Format Based on the Webster's Dictionary 1913 Edition
Content
This is the full OPTED version of a Public Domain dictionary based on the Webster's Unabridged Dictionary, 1913 edition. The CSV file contains all entries, along with the character count for each word, the Part of Speech, and the Definition.

### Code

- I found help on <https://stackoverflow.com/>
- I also used CodeInstitute examples

### Content

- All content was written by myself

### Media

- no images were used for this project

## Deployment

1. Create an account with Heroku (could not find my GitHub Student Developer Pack, in my spam either)
2. Log in to Heroku
3. Create an app with Heroku after giving my credit card infos
4. In settings giving Config Vars, also the 'PORT' one. Giving also two Buildpacks : python and nodejs
5. Connecting Heroku to my Git Hub and locat the [GitHub Repository](https://github.com/Cyril-CRGB/Portfolio3_Python_Essentials.git)
6. Then Deploy manually the application

## Find this web site:

[My Second Project live](https://portfolio3-python-essentials-d35a77840b91.herokuapp.com/)

[My page on GitHub](https://github.com/Cyril-CRGB/Portfolio3_Python_Essentials.git)