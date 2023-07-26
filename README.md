# Portfolio 3 - Python Essential

## Distribution key calculator

## Project description

This website is an idea that I received from someone I am following on LinkedIn who works for public transportation. He asked his network a very interesting question. This project tries to answer that question.

A fare community regroupes a lot of bus, train, boat companies. The question raised was how can we share the revenue of a ticket or subscription which valid on the whole network. 

This app use data from two google sheet and performs calculations to get to the result! 

google sheet 1 : Portfolio3_distribution_keys

google sheet 2 : Portfolio3_distribution_keys_2

The final keys on worksheet "Keys" must sum up to 100% when added.

Unfortunately, there is a limitation to what a user can write into google sheet through 1 google project. This is the reason why I used two separate google sheet. Unfortunately Herku does not allow me to use more than 1 credential .json file. 

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
- could not access rows with "row['sheetname']", needed to use index
- cant convert string to float with "float(string)", I need to replace "," by "."
- cant convert null to integers or float, need to writh to try-except fonction to handle each of them
- cant use function convert_to_float to convert percent
- dealing with 'status' : 'RESOURCE_EXHAUSTED' from 'sheets.googleapis.com'
- dealing with 'cannot find creds2.json' after deploying on heroku

## Technologies Used

- Python

## Special library

- numpy (fonction "Calculate_regression")
- pandas (fonction "Calculate_regression")

## Credits

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