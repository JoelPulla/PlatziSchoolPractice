"""Reto Plazi transformar """

#Transformar de csv a json 
import csv
import json 

csv_path = "Programacion basica/python/Lectura y escritura de archivos/products.csv"
csv_json = "Programacion basica/python/Lectura y escritura de archivos/csv_a_json.json"

with open(csv_path, 'r') as file:
    products = csv.DictReader(file)
    
    list_product = []
    
    for product in products:
        list_product.append(product)
        
with open(csv_json, mode='w') as file:
    json.dump(list_product, file, indent=4)
    
    print('Se comvirtio de csv a json correctamente')
    
    
