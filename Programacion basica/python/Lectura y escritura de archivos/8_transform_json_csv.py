"""Reto platzi Json a Csv"""

#Trannsformar un archivo json a formato csv 

import json
import csv


json_path = "Programacion basica/python/Lectura y escritura de archivos/example.json"
json_csv = "Programacion basica/python/Lectura y escritura de archivos/json_a_csv.csv"


with open(json_path, 'r') as file:
    movies = json.load(file) # lee
    #claves del json 
    keys_json = movies[0].keys()
    
    #valores de nuestra json 
    for content in movies:
        values_json = content.values()
        
with open(json_csv, mode='w',newline='') as update_file:
        csv_writer = csv.DictWriter(update_file, fieldnames=keys_json)
        csv_writer.writeheader()

        for content in movies:
            csv_writer.writerow(content)

        print('Se transformado el archivo correctamente')

