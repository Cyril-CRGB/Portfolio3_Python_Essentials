buggs : 
- could not access rows with "row['sheetname']", needed to use index
- cant convert string to float with "float(string)", I need to replace "," by "."
- cant convert null to integers or float, need to writh to try-except fonction to handle each of them
- cant use function convert_to_float to convert percent
- dealing with 'status' : 'RESOURCE_EXHAUSTED' from 'sheets.googleapis.com'

nettoyage du code à faire :
- supprimer # print()

import de librairies spéciales : 
numpy (fonction "Calculate_regression")
pandas (fonction "Calculate_regression")

# Portfolio 2 - Javascript Essentials

## Cross-Border Ski Resort Fare Calculator

<img src="assets/images/Portfolio2_Readme_AmIResponsive.jpg" alt="ReadmePicture1">

## Project description

This website is an idea that I received from a friend who loves skiing in the Alpes : [les portes du soleil](https://www.portesdusoleil.com/).

Their is a lot of cable car companies, and if we want the client to be able to use all the equipement with one ticket. We need to find a way to calculate the right fare.

This website is made for it!

The data used is only for exemple.

## Features:

Each Cable car company fare liste is listed as a grey table, here 1 swiss and 2 french, namely A, B, C.<img src="assets/images/Portfolio2_Readme_Feature1.jpg" alt="ReadmePicture2">

Each article is given in two currencies CHF (Swiss francs) and EURO (euros). Each table is either originaly given in CHF or EURO, and this is indicated by blue color, the other column is calculated. <img src="assets/images/Portfolio2_Readme_Feature2.jpg" alt="ReadmePicture3">

Blue colored prices are editable when you click on it. <img src="assets/images/Portfolio2_Readme_Feature3.jpg" alt="ReadmePicture4">

If you change blue prices, the change will be effective if you click somewhere else and an alert pops up and tell the user to click on "Calculate rate" button.<img src="assets/images/Portfolio2_Readme_Feature4.jpg" alt="ReadmePicture5">

At the top right of the screen there is an input text and a button called "Calculate rate" which allows you to change the rate 1€ = CHF ?
If you change the rate and click on "Calculate rate" all the black colored price are recalculated and put in orange color. <img src="assets/images/Portfolio2_Readme_Feature5.jpg" alt="ReadmePicture6">

At the top left, you will find two other buttons. The first "Generate list of Prices" will update the yellow table with a list of all 6 articles with the cumulative prices of table1, table2 and table3 in column Price CHF and Price EURO. The second "Generate Excel list" allows the user to export in excel file the yellow table. <img src="assets/images/Portfolio2_Readme_Feature6.jpg" alt="ReadmePicture7">

If the yellow table does not contain any data, the user will receive an alert that the data is empty.<img src="assets/images/Portfolio2_Readme_Feature7.jpg" alt="ReadmePicture8">

## Testing:

I do not know if the following are truly bugs, but those are were I struggled the most.

- Bug fix 1: I initially wanted to have each cable car fare table in a separate html file, but I could not retrieve the data inside my script.js file. I know it is possible to do it using "localstorage", yet I had not time to implement it.
- Bug fix 2: at first I tried to move through the table in order to get/replace values in it, using: "table1.rows[i].cells[i]". But it was not working. I used ".children" instead of ".rows" and ".cells" and it worked like a charm.
- Bug fix 3: I was not able to give relative length to my loops, so I decided to use absolute length. This is something I would like to change if I were to give this website to my friend.

- I tested the HTML code with https://validator.w3.org/#validate_by_input : no error found
  <img src="assets/images/Portfolio2_Readme_htmlValidator.jpg" alt="ReadmePicture2">
- I tested the CSS code with https://jigsaw.w3.org/css-validator/#validate_by_input : no error found
  <img src="assets/images/Portfolio2_Readme_cssValidator.jpg" alt="ReadmePicture3">
- I tested the Javascript code with https://jshint.com/ : no error found, yet 43 warnings, mainly about the compatibility of 'let' used to define variables as well as 'template literal syntax', loops referencing an outer scoped variable. Also it cannot find a variable 'XLSX' yet it is working!
  <img src="assets/images/Portfolio2_Readme_jshintValidator.jpg" alt="ReadmePicture4">
- I tested different web browsers Chrome and Edge : working on both
- I tested different screen sizes, and different devices : the website is responsive

## The performances of my first project:

I had to use private navigator, it seems like some of the code is not compatible with new generation browsers. I did not add meta description, since it is said that HTML/CSS is not the main topic of this project [see video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+JSE_PAGPPF+2021_Q2/courseware/30137de05cd847d1a6b6d2c7338c4655/c3bd296fe9d643af86e76e830e1470dd/), which explains the result of 82 for SEO.
<img src="assets/images/Portfolio2_Readme_LighthousPerformance.jpg" alt="ReadmePicture5">

## Technologies Used

- HTML5
- CSS3
- Javascript

## Special library

- Excel : https://unpkg.com/xlsx/dist/xlsx.full.min.js

## Credits

### Code

- I found help on <https://stackoverflow.com/>
- I also used CodeInstitute examples

### Content

- All content was written by myself

### Media

- no images were used for this project

## Deployment

1. Log in to GitHub and locat the [GitHub Repository](https://github.com/Cyril-CRGB/Portfolio2_JavaScript_Essentials.git)
2. At the top of the Repository, locate the "Settings" Button on the menu.
3. At the left of the new window, find the "Page" Button under "Code and automation"
4. At the section "Branch" select "Main", then "Root" and clic "Save"
5. Wait until the link shows up, there you go !

## Find this web site:

[My Second Project live](https://portfolio3-python-essentials-d35a77840b91.herokuapp.com/)

[My page on GitHub](https://github.com/Cyril-CRGB/Portfolio2_JavaScript_Essentials.git)