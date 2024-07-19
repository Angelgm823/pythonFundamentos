#creacion de csv
import csv
datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ignacio", "20", "CDMX"],
    ["Raul", "30", "Iztapalapa"],
    ["Rosa", "24", "Ixtapaluca"],
    ["Yair", "25", "Xalpa"],
]
with open ("personas.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(datos)
    
#lectura de csv

import csv
with open("personas.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
#lectura con DictReader()

import csv
with open('personas.csv') as file:
    obj = csv.DictReader(file)
    for item in obj:
        print(item['Nombre'] + ' vive en ' + item["Ciudad"]  + item["Edad"] + 'años.')