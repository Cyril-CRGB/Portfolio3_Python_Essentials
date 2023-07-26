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
<img src="assets/images/Portfolio2_Readme_Feature1.jpg" alt="ReadmePicture2">

This app contains 1 global function, 12 major functions and 4 minor functions.

The global function calls the 12 major and the 12 major call the 4 minor for calulation purpose.

The global function is called: 
<ul>main</ul>
The 12 major functions are called: 
<ol>calculate_t_significant</ol>
<ol>calculate_pk_significant</ol>
<ol>calculate_structure_2</ol>
<ol>update_sum_column_structure_2</ol>
<ol>calculate_percent_structure_3</ol>
<ol>alculate_average_km</ol>
<ol>calculate_regression</ol>
<ol>calculate_total_average_pk</ol>
<ol>calculate_totalprice</ol>
<ol>calculate_sharetravellers</ol>
<ol>calculate_sharePassengerkilometers</ol>
<ol>calculate_keys</ol>
The 4 minor functions are called:
<ol>verify_significant</ol>
<ol>convert_to_int</ol>
<ol>convert_to_float</ol>
<ol>find_percentage</ol>

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