# Portfolio 3 - Python Essential

## Word guess game

## Project description

This website is a word game based on a free english dictionary. 

The goal for the end user is to test his/her knowledges of the english language, and learn new words.

The client can chose between two ways of playing. Either try to guess the definition of a given word, or the opposite, try to guess a word of a given definition.

Word and definition that the client is looking for are randomly chosen and given by the programm.

The client can then chose amongs 3 solutions, only one of them is true, the 2 others are randomly chosen by the programm. No repeatition is allowed. The solution suggested by the programm must be different from one another.

Have fun with the game, and learn new words!


## Features:

This app contains 1 global function, 12 major functions and 4 minor functions.

The global function calls the 12 major and the 12 major call the 4 minor for calulation purpose.

The global function is called: 
<li>main</li>
The 12 major functions are called: 
<li>calculate_t_significant</li>
<li>calculate_pk_significant</li>
<li>calculate_structure_2</li>
<li>update_sum_column_structure_2</li>
<li>calculate_percent_structure_3</li>
<li>alculate_average_km</li>
<li>calculate_regression</li>
<li>calculate_total_average_pk</li>
<li>calculate_totalprice</li>
<li>calculate_sharetravellers</li>
<li>calculate_sharePassengerkilometers</li>
<li>calculate_keys</li>
The 4 minor functions are called:
<li>verify_significant</li>
<li>convert_to_int</li>
<li>convert_to_float</li>
<li>find_percentage</li>

## Testing:
buggs : 
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

Dealing with exception:
By the functions "guess_word" and "guess_definition", if an Invalid input is given, it takes the player out of the function, back to the "main" function, although the player might still want to keep trying.

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