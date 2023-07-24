buggs : 
- could not access rows with "row['sheetname']", needed to use index
- cant convert string to float with "float(string)", I need to replace "," by "."
- cant convert null to integers or float, need to writh to try-except fonction to handle each of them
- cant use function convert_to_float to convert percent
- dealing with 'status' : 'RESOURCE_EXHAUSTED' from 'sheets.googleapis.com'

nettoyage du code à faire :
- supprimer # print()